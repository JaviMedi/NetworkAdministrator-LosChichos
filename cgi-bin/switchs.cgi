#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

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

accio=$(echo "$QUERY_STRING" | sed -n 's/^.*accio=\([^&]*\).*$/\1/p')
ORDRE="switchs "


if [ "$accio" == "desactivar_acl_admin" ] || [ "$accio" == "desactivar_acl_macs" ] || [ "$accio" == "activar_acl_admin" ] || [ "$accio" == "activar_acl_macs" ]; then
	ORDRE+="configurar $accio $(echo "$QUERY_STRING" | sed -n 's/^.*ip=\([^&]*\).*$/\1/p')"
elif [ "$accio" == "iniciar" ]; then
	ORDRE+="iniciar"
elif [ "$accio" == "aturar" ]; then
	ORDRE+="aturar"
fi

RESULTAT=$(/usr/local/LosChichos/system/nc_client "$ORDRE" 2>&1)
echo "<pre>$RESULTAT</pre>"


/bin/cat <<EOM
</body>
</html>
EOM
