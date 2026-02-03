#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ebtables Configuration</title>
EOM
cat /usr/local/LosChichos/cgi-bin/css.txt
/bin/cat << EOM
</head>
<body>
    <h1>Configuración de Aislamiento de VLANs</h1>
EOM

# Loop over VLANs
for LINIA in $(grep -v '^#' "$DIR/$PROJECTO/$DIR_CONF/$BRIDGE_CONF"); do
    NOM=$(echo "$LINIA" | cut -d';' -f1)
    ID=$(echo "$LINIA" | cut -d';' -f2)
    IP=$(echo "$LINIA" | cut -d';' -f3)

    # Check status using the script
    STATUS=$(/usr/local/LosChichos/scripts/ebtables estat $ID)
    
    if [ "$STATUS" == "AISLADA" ]; then
        echo "<h2>  $NOM (VLAN $ID) $IP <span class='status-yellow'>AISLADA</span></h2>"
        echo "<a href='ebtables-exec.cgi?action=desaislar&id=$ID'><button type='button'>DESAISLAR</button></a>"
    else
        echo "<h2>  $NOM (VLAN $ID) $IP <span class='status-green'>NO AISLADA</span></h2>"
        echo "<a href='ebtables-exec.cgi?action=aislar&id=$ID'><button type='button'>AISLAR</button></a>"
    fi
     echo "<br>"
done

/bin/cat << EOM
</body>
</html>
EOM
