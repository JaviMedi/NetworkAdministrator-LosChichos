#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

# -------------------------------------------------------------------
# Decodificar parámetros GET
# -------------------------------------------------------------------
QUERY_STRING_DECODED=$(echo "$QUERY_STRING" | sed 's/+/ /g; s/%/\\x/g' | xargs -0 printf "%b")
VID_PARAM=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*vid=\([^&]*\).*/\1/p')

# -------------------------------------------------------------------
# Obtener la VLAN correspondiente
# -------------------------------------------------------------------
VLAN_DATA=$(/usr/local/LosChichos/system/nc_client "bridge conf show vlan")
LINE=$(echo "$VLAN_DATA" | grep -E ";$VID_PARAM;" || true)

if [ -z "$LINE" ]; then
    echo "<html><body><h3 style='color:red;'>No se encontró la VLAN con VID $VID_PARAM</h3></body></html>"
    exit 0
fi

IFS=';' read -r nombre vid subnet gw _ <<< "$LINE"

# -------------------------------------------------------------------
# HTML
# -------------------------------------------------------------------
/bin/cat << EOM
<html>
<head>
<meta charset="utf-8">
<title>Modificar VLAN $vid</title>
<style>
body {
  font-family: Arial, sans-serif;
  background-color: #f6f6f6;
  color: #333;
  margin: 20px;
}
h2 {
  background-color: #003366;
  color: white;
  padding: 10px;
  border-radius: 5px;
}
table {
  border-collapse: collapse;
  width: 60%;
  background: white;
  box-shadow: 0 0 5px rgba(0,0,0,0.2);
}
td, th {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}
th {
  background-color: #e9edf2;
}
input[type=text] {
  width: 95%;
  padding: 5px;
  border: 1px solid #aaa;
  border-radius: 3px;
}
button {
  padding: 8px 15px;
  background-color: #003366;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #0055aa;
}
</style>
</head>
<body>

<h2>Modificar VLAN (VID: $vid)</h2>

<form method="get" action="/cgi-bin/bridge.cgi">
  <!-- Campos ocultos -->
  <input type="hidden" name="comand" value="conf">
  <input type="hidden" name="mode" value="guardar">
  <input type="hidden" name="v_b" value="vlan">
  <input type="hidden" name="vid" value="$vid">
  <input type='hidden' name='redirect' value='cgi-bin/bridge-configurar.cgi'>

  <table>
    <tr><th>Campo</th><th>Valor</th></tr>
    <tr><td>Nombre</td><td><input type="text" name="nombre" value="$nombre"></td></tr>
    <tr><td>VID</td><td><b>$vid</b></td></tr>
    <tr><td>Subred</td><td><input type="text" name="subnet" value="$subnet"></td></tr>
    <tr><td>Gateway</td><td><input type="text" name="gw" value="$gw"></td></tr>
  </table>

  <br>
  <button type="submit">Guardar cambios</button>
  <button type="button" onclick="window.history.back()">Cancelar</button>
</form>

</body>
</html>
EOM
