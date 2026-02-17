#!/bin/bash


source /usr/local/LosChichos/conf/variables.conf
source $DIR/$PROJECTE/$DIR_CONF/$CONF_IFWAN



interfaces=$(ls /sys/class/net)
WAN_IF=$(ip route show default | awk '/default/ {print $5}')

interfaces_filtradas=()
for iface in $interfaces; do
  if [[ "$iface" == "lo" ]]; then
    continue  
  fi
  if [[ $iface == br* ]]; then  
    continue  
  fi
  if [[ -d "/sys/class/net/$iface/wireless" ]]; then
    continue  
  fi
  if [[ "$iface" == "$WAN_IF" ]]; then
    continue
  fi
  interfaces_filtradas+=("$iface")
done


echo "Content-type: text/html; charset=utf-8"
echo ""

VLAN_DATA=$(/usr/local/LosChichos/system/nc_client "bridge conf show bridge")

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
EOM
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


echo "<h2>Configuració Tag-Untag</h2>"

echo "<table>"
echo "<tr><th>Interfaz</th><th>UNTAG</th><th>TAG</th><th></th></tr>"
for enp in "${interfaces_filtradas[@]}"; do
	echo "<tr><td>$enp</td>"
	linia_int=$(echo "$VLAN_DATA" | grep -E "^${enp};")
	VLAN_UNTAG=$(echo "$linia_int"|cut -d';' -f2)
	if [[ -z "$VLAN_UNTAG" ]]; then
	    echo "<td>0</td>"
	else
	    echo "<td>$VLAN_UNTAG</td>"
	fi
	VLAN_TAG=$(echo "$linia_int"|cut -d';' -f3)
	if [[ -z "$VLAN_TAG" ]]; then
	    echo "<td>0</td>"
	else
	    echo "<td>$VLAN_TAG</td>"
	fi
	echo "<td><button onclick=\"location.href='/cgi-bin/bridge-modificar-taguntag.cgi?enp=$enp'\">Modificar</button></td></tr>"
done
echo "</table>"

/bin/cat << EOM
</body>
</html>
EOM


