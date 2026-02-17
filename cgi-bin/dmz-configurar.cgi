#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf
source $DIR/$PROJECTO/$DIR_CONF/$CONF_IFWAN

Interfaces_Ethernet() {
    for iface in $(ip -o link show | awk -F': ' '{print $2}'); do
        if [[ "$iface" != "lo" ]] && [[ "$iface" != "$IFW_IFWAN" ]] && [[ $iface != br0* ]]; then
            if ! iw dev 2>/dev/null | grep -qw "$iface"; then
                echo "$iface"
            fi
        fi
    done
}


echo "Content-type: text/html; charset=utf-8"
echo ""

#VLAN_DATA="$("$DIR"/"$PROJECTE"/"$DIR_SCRIPTS"/client_srv_cli bridge configurar mostrar bridge)"
VLAN_DATA=$(cd "$DIR"/"$PROJECTO"/"$DIR_SCRIPTS"/ && ./bridge conf show vlan bridge)

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
EOM

echo "</head><body>"

cat $DIR/$PROJECTO/$DIR_CGI/$CSS_CGI_BIN

echo "<h2>Configuració DMZ</h2>"

echo "<table>"
echo "<tr><th>Port</th><th>Protocol</th><th>ip</th><th></th></tr>"


for iface in $(/usr/local/LosChichos/system/nc_client "dmz configurar mostrar"); do
	PORT=$(echo "$iface"|cut -d';' -f1)
	PROTO=$(echo "$iface"|cut -d';' -f2)
	IP_DMZ=$(echo "$iface"|cut -d';' -f3)
	
	echo "<tr><td>$PORT</td><td>$PROTO</td><td>$IP_DMZ</td>"
	
	echo "<td><button onclick=\"location.href='/cgi-bin/dmz-eliminar.cgi?port=$PORT&proto=$PROTO&ipdmz=$IP_DMZ'\">Eliminar</button></td></tr>"
done
echo "</table>"

echo "<button onclick=\"location.href='/cgi-bin/dmz-nou-servei.cgi'\">Obrir nou servei</button>"

/bin/cat << EOM
</body>
</html>
EOM



