#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf
source $DIR/$PROJECTO/$DIR_CONF/$FUNC

echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat <<EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
EOM
cat $DIR/$PROJECTO$DIR_CGI/$CSS_CGI_BIN
/bin/cat <<EOM
</head>
<body>
EOM


echo "<h2>Tablas MACs</h2>"


RESULTAT=$(/usr/local/LosChichos/system/nc_client "switchs totes_les_taula_mac" 2>&1)
in_table=0

while IFS= read -r raw_linia; do
    linia=$(echo "$raw_linia" | tr -d '\r')
    # Si la línia comença amb "Switch ", és un nou switch
    if [[ $linia =~ ^Switch ]]; then
        if [[ $in_table -eq 1 ]]; then
            echo "</tbody></table>"
            echo "<br>"
        fi
        echo "<h3>$linia</h3>"
        echo "<table>"
        echo "<thead><tr><th>MAC</th><th>IP</th><th>VLAN</th><th>Port</th><th>Type</th><th></th></tr></thead>"
        echo "<tbody>"
        in_table=1
    # Si la línia té format de MAC (xx:xx:xx:xx:xx:xx)
    elif [[ $linia =~ ^[[:space:]]*([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2} ]]; then
        read -r mac vlan port type aging <<< "$linia"
        INFO_MAC=$(fnc_ip_de_mac $mac)
        if [ -z "$INFO_MAC" ]; then
            INFO_MAC=$(fnc_mac_propia $mac)
        fi
        echo "<tr><td>$mac</td><td>$INFO_MAC</td><td>$vlan</td><td>$port</td><td>$type</td><td><a href='/cgi-bin/switchs-blocar-mac.cgi?accio=blocar&mac=$mac'><button type=\"button\">Bloquear</button></a></td></tr>"
    # Si la línia és el resum final d'un switch
    elif [[ $linia =~ ^[[:space:]]*Total[[:space:]]MAC[[:space:]]Addresses ]]; then
        if [[ $in_table -eq 1 ]]; then
            echo "</tbody></table>"
            in_table=0
        fi
        echo "<p><strong>$linia</strong></p>"
        echo "<br>"
    fi
done <<< "$RESULTAT"

if [[ $in_table -eq 1 ]]; then
    echo "</tbody></table>"
fi

echo "<br>"

/bin/cat <<EOM
</body>
</html>
EOM