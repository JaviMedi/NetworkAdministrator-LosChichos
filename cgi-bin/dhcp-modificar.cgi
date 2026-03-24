#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

QUERY_STRING=${QUERY_STRING:-$1}
VID=$(echo "$QUERY_STRING" | sed -n 's/.*vid=\([0-9]*\).*/\1/p')

echo "<html><head><title>Modificar DHCP VLAN</title>"
echo "<meta charset='utf-8'>"
cat $DIR/$PROJECTO/$DIR_CGI/$CSS_CGI_BIN
echo "</head><body>"

VLAN_DATA="$(/usr/local/LosChichos/system/nc_client "dhcp configurar mostrar_conf")"
mapfile -t VLANS <<<"$VLAN_DATA"

FOUND_LINE=""
for line in "${VLANS[@]}"; do
	IFS=';' read -r vid inici final gateway dns1 dns2 activat <<<"$line"
	if [ "$vid" == "$VID" ]; then
		FOUND_LINE="$line"
		break
	fi
done

if [ -z "$FOUND_LINE" ]; then
	echo "<p><b>Error:</b> No s'ha trobat cap VLAN amb VID = $VID</p>"
	echo "</body></html>"
	exit 0
fi

IFS=';' read -r vid inici final gateway dns1 dns2 activat <<<"$FOUND_LINE"

echo "<h2>Modificar VLAN</h2>"
echo "<form action='/cgi-bin/dhcp.cgi' method='get'>"
echo "<input type='hidden' name='comand' value='configurar'>"
echo "<input type='hidden' name='accio' value='guardar_conf'>"
echo "<table>"
echo "<tr><th>VID</th><th>inici</th><th>final</th><th>gateway</th><th>dns1</th><th>activat</th></tr>"
echo "<tr>"
echo "<td><input type='text' name='vid' value='$vid' size='3' readonly></td>"
echo "<td><input type='text' class='ip' name='inici' value='$inici' size='15'></td>"
echo "<td><input type='text' class='ip' name='final' value='$final' size='15'></td>"
echo "<td><input type='text' class='ip' name='gateway' value='$gateway' size='15'></td>"
echo "<td><input type='text' class='ip' name='dns1' value='$dns1' size='15'></td>"
echo "<td><select name='activat'>"
if [ "$activat" == "$ACTIVADO" ]; then
	echo "<option value='$ACTIVADO' selected>$ACTIVADO</option>"
	echo "<option value='$DESACTIVADO'>$DESACTIVADO</option>"
else
	echo "<option value='$ACTIVADO'>$ACTIVADO</option>"
	echo "<option value='$DESACTIVADO' selected>$DESACTIVADO</option>"
fi
echo "</select></td>"
echo "</tr>"
echo "</table>"
echo "<button type='submit'>Guardar</button>"
echo "</form>"

echo "</body></html>"
