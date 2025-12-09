#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

interfaces=$(ls /sys/class/net)

interfaces_filtradas=()
for iface in $interfaces; do
  if [[ "$iface" == "lo" ]]; then
    continue  
  fi
  if [[ -d "/sys/class/net/$iface/wireless" ]]; then
    continue  
  fi
  if [[ "$iface" == br* ]]; then
    continue  
  fi
  interfaces_filtradas+=("$iface")
done

CONFIG=$(cd "$DIR"/"$PROJECTO"/"$DIR_SCRIPTS"/ && ./ifwan conf mostrar)
conf_mode=$(echo "$CONFIG" | tr -s ' ' | cut -d' '  -f1 )
conf_int=$(echo "$CONFIG" | tr -s ' ' | cut -d' '  -f2 )
conf_ip=$(echo "$CONFIG" | tr -s ' ' | cut -d' '  -f3 )
conf_masc=$(echo "$CONFIG" | tr -s ' ' | cut -d' '  -f4 )
conf_pe=$(echo "$CONFIG" | tr -s ' ' | cut -d' '  -f5 )
conf_dns=$(echo "$CONFIG" | tr -s ' ' | cut -d' ' -f6 )


/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Configura-ifwan</title>
  <style>
body {
  font-family: Arial, sans-serif;
  background-color: #eef3f8;
  color: #333;
  margin: 0;
  padding: 0;
}
.header {
  background-color: #003366;
  color: white;
  padding: 15px;
  text-align: center;
  font-size: 1.5em;
  font-weight: bold;
}
h3 {
  background: #f2f6fa;
  border-left: 5px solid #003366;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
}
.router-button {
  background-color: #003366;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 10px 25px;
  font-size: 1em;
  font-weight: bold; 
  cursor: pointer; 
  margin: 5px; 
  box-shadow: 0px 2px 5px rgba(0,0,0,0.3); 
  transition: all 0.2s ease-in-out;
}

.router-button:hover {
  background-color: #0055aa; 
  box-shadow: 0px 4px 8px rgba(0,0,0,0.4);
}

.hidden-fields {
  display: none; /* Ocultos por defecto */
  margin-top: 10px;
}
  </style>
  <script>
function toggleManualFields() {
  var manualSelected = document.getElementById('manual').checked;
  var fields = document.getElementById('manualFields');
  fields.style.display = manualSelected ? 'block' : 'none';
}

window.addEventListener('DOMContentLoaded', function() {
  toggleManualFields();
});
</script>
</head>
<body>

<h3> Configuració ifwan</h3>

<h4>Modo de la Interfaz WAN</h4>

<form action="/cgi-bin/ifwan.cgi" method="get">

EOM

      dhcp_check=""
      manual_check=""
      if [[ "$conf_mode" == "manual" ]] then
        manual_check="checked"
      else  
       dhcp_check="checked"
      fi



  echo '<input type="radio" id="dhcp" name="mode" value="dhcp" '$dhcp_check' onclick="toggleManualFields()">'
 
   echo '<label for="dhcp">DHCP</label><br>'

  echo '<input type="radio" id="manual" name="mode" value="manual" '$manual_check' onclick="toggleManualFields()">'
  echo '<label for="manual">Manual</label><br><br>'
/bin/cat << EOM
<h4>Nombre de la Interfaz WAN</h4>
EOM

for iface in "${interfaces_filtradas[@]}"; do
  if [ "$iface" == "$conf_int" ]; then 
    echo "  <input type=\"radio\" id=\"$iface\" name=\"interface\" value=\"$iface\" checked>"
  else
    echo "  <input type=\"radio\" id=\"$iface\" name=\"interface\" value=\"$iface\">"
  fi
  echo "  <label for=\"$iface\">$iface</label><br>"
done

cat << EOM
<br>
<div id="manualFields" class="hidden-fields">
  <h4>Dirección IP y máscara</h4>
EOM
  echo "<input type="text" name="ipmask" value= "$conf_ip"/"$conf_masc"><br><br>"
cat << EOM
  <br>
  <h4>Dirección de Gateway</h4>
EOM
  echo "<input type="text" name="gtw" value='$conf_pe' placeholder="Ej: 192.168.1.1"><br><br>"
cat << EOM
  <br>
  <h4>Dirección de Servidor DNS</h4>
EOM
  echo "<input type="text" name="dns" value='$conf_dns' placeholder="Ej: 8.8.8.8"><br><br>"
cat << EOM
  <br>
</div>

<input type="submit" class="router-button" name="comand" value="conf">
</form>
</body>
</html>
EOM