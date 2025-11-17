#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf


echo "Content-type: text/html; charset=utf-8"
echo ""

echo "<html><head><title>Crear VLAN</title>"
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

echo "<h2>Crear VLAN</h2>"
echo "<form action='/cgi-bin/bridge.cgi' method='get'>"
echo "<input type="hidden" name="comand" value="conf">"
echo "<input type="hidden" name="mode" value="guardar">"
echo "<input type="hidden" name="v_b" value="vlan">"
echo "<input type='hidden' name='redirect' value='cgi-bin/bridge-configurar.cgi'>"
echo "<table>"
echo "<tr><th>Nom</th><th>VID</th><th>IP/Subred</th><th>IP/Gateway</th></tr>"
echo "<tr>"
# Nom ara també més ample
echo "<td><input type='text' name='nombre' value='' style='width: 250px;'></td>"
# VID només lectura
echo "<td><input type='text' name='vid' value='' ></td>"
# Camps IP més amplis
echo "<td><input type='text' class='ip' name='subnet' value=''></td>"
echo "<td><input type='text' class='ip' name='gw' value=''></td>"
echo "</tr>"
echo "</table>"
echo "<button type='submit'>Crear</button>"
echo "</form>"
echo "</body></html>"