#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf


echo "Content-type: text/html; charset=utf-8"
echo ""


raw_enp=$(echo "$QUERY_STRING" | sed -n 's/^.*enp=\([^&]*\).*$/\1/p')
enp=$(printf '%b' "${raw_enp//%/\\x}")

echo "<html><head><title>Modificar VLAN</title>"
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
linia_int=$(echo "$VLAN_DATA" | grep -E "^${enp};")
VLAN_UNTAG=$(echo "$linia_int"|cut -d';' -f2)
if [[ -z "$VLAN_UNTAG" ]]; then
	   VLAN_UNTAG=0
fi
VLAN_TAG=$(echo "$linia_int"|cut -d';' -f3)
if [[ -z "$VLAN_TAG" ]]; then
	   VLAN_TAG=0
fi

echo "<h2>Modificar Tag-Untag</h2>"
echo "<form action='/cgi-bin/bridge.cgi' method='get'>"
echo "<input type="hidden" name="comand" value="conf">"
echo "<input type="hidden" name="mode" value="guardar">"
echo "<input type="hidden" name="v_b" value="bridge">"
echo "<input type='hidden' name='redirect' value='cgi-bin/bridge-configurar-taguntag.cgi'>"
echo "<table>"
echo "<tr><th>Interfaç</th><th>Untag</th><th>Tag</th></tr>"
echo "<tr>"


echo "<td><input type='text' name='enp' value='$enp' style='width: 250px;' readonly></td>"   
echo "<td><input type='text' class='untag' name='untag' value='$VLAN_UNTAG'></td>"
echo "<td><input type='text' class='tag' name='tag' value='$VLAN_TAG'></td>"
echo "</tr>"
echo "</table>"
echo "<button type='submit'>Guardar</button>"
echo "</form>"

echo "</body></html>"
