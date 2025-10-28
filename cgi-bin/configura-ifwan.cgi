#!/bin/bash
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
  interfaces_filtradas+=("$iface")
done
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
</script>
</head>
<body>

<h3> Configuració ifwan</h3>

<h4>Modo de la Interfaz WAN</h4>

<form action="/cgi-bin/ifwan.cgi" method="get">
  <input type="radio" id="dhcp" name="mode" value="dhcp" checked onclick="toggleManualFields()">
  <label for="dhcp">DHCP</label><br>

  <input type="radio" id="manual" name="mode" value="manual" onclick="toggleManualFields()">
  <label for="manual">Manual</label><br><br>

<h4>Nombre de la Interfaz WAN</h4>
EOM

for iface in "${interfaces_filtradas[@]}"; do
  echo "  <input type=\"radio\" id=\"$iface\" name=\"interface\" value=\"$iface\">"
  echo "  <label for=\"$iface\">$iface</label><br>"
done

cat << EOM
<br>
<div id="manualFields" class="hidden-fields">
  <h4>Dirección IP y máscara</h4>
  <input type="text" name="ipmask" placeholder="Ej: 192.168.1.100/24"><br><br>
  <br>
  <h4>Dirección de Gateway</h4>
  <input type="text" name="gtw" placeholder="Ej: 192.168.1.1"><br><br>
  <br>
  <h4>Dirección de Servidor DNS</h4>
  <input type="text" name="dns" placeholder="Ej: 8.8.8.8"><br><br>
  <br>
</div>

<input type="submit" class="router-button" name="comand" value="conf">
</form>
</body>
</html>
EOM