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
mac=$(echo "$QUERY_STRING" | sed -n 's/^.*mac=\([^&]*\).*$/\1/p'| sed 's/%3[aA]/:/g')
echo "<pre>"
if [ "$accio" == "blocar" ]; then
  echo "$(/usr/local/LosChichos/system/nc_client "switchs configurar blocar_mac $mac" 2>&1) <br>"
elif [ "$accio" == "desblocar" ]; then
  echo "$(/usr/local/LosChichos/system/nc_client "switchs configurar desblocar_mac $mac" 2>&1) <br>"
fi
echo "</pre>"

/bin/cat <<EOM
</body>
</html>
EOM
