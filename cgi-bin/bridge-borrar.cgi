#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf


echo "Content-type: text/html; charset=utf-8"
echo ""


QUERY_STRING=${QUERY_STRING:-$1}  
VID=$(echo "$QUERY_STRING" | sed -n 's/.*vid=\([0-9]*\).*/\1/p')

echo "<html><head><title>Esborrar  VLAN</title>"
echo "<meta charset='utf-8'>"
echo "
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
</style>"
echo "</head><body>"

VLAN_DATA=$(cd "$DIR"/"$PROJECTO"/"$DIR_SCRIPTS"/ && ./bridge conf show vlan)

mapfile -t VLANS <<< "$VLAN_DATA"

FOUND_LINE=""
for line in "${VLANS[@]}"; do
    IFS=';' read -r nombre vid subnet gw _ <<< "$line"
    if [ "$vid" == "$VID" ]; then
        FOUND_LINE="$line"
        break
    fi
done

if [ -z "$FOUND_LINE" ]; then
    echo "<p><b>Error:</b> No se ha encontrado ninguna vlan con el vid = $VID</p>"
    echo "</body></html>"
    exit 0
fi

IFS=';' read -r nombre vid subnet gw _ <<< "$FOUND_LINE"

echo "<h2>Borrar VLAN</h2>"
echo "<form action='/cgi-bin/bridge.cgi' method='get'>"
echo "<input type="hidden" name="comand" value="conf">"
echo "<input type="hidden" name="mode" value="borrar">"
echo "<input type="hidden" name="v_b" value="vlan">"
echo "<input type="hidden" name="vid" value="$vid">"
echo "<input type='hidden' name='redirect' value='cgi-bin/bridge-configurar.cgi'>"
echo "<table>"
echo "<tr><th>Nom</th><th>VID</th><th>IP/Subred</th><th>IP/Gateway</th></tr>"
echo "<tr>"
# Nom ara també més ample
echo "<td><b>$nombre</b></td>"
# VID només lectura
echo "<td><b>$vid</b></td>"
# Camps IP més amplis
echo "<td><b>$subnet</b></td>"
echo "<td><b>$gw</b></td>"
echo "</tr>"
echo "</table>"
echo "<button type='submit'>Borrar</button>"
echo "</form>"

echo "</body></html>"