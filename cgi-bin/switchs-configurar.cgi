#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat <<EOM
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="1; url=/cgi-bin/switchs.cgi?comand=estat&">
  <title>Hola món CGI</title>
EOM
cat $DIR/$PROJECTO$DIR_CGI/$CSS_CGI_BIN
/bin/cat <<EOM
</head>
<body>
EOM


accio=$(echo "$QUERY_STRING" | sed -n 's/^.*accio=\([^&]*\).*$/\1/p')
nom=$(echo "$QUERY_STRING" | sed -n 's/^.*nom=\([^&]*\).*$/\1/p')
ip=$(echo "$QUERY_STRING" | sed -n 's/^.*ip=\([^&]*\).*$/\1/p')
user=$(echo "$QUERY_STRING" | sed -n 's/^.*user=\([^&]*\).*$/\1/p')
pass=$(echo "$QUERY_STRING" | sed -n 's/^.*pass=\([^&]*\).*$/\1/p')
protocol=$(echo "$QUERY_STRING" | sed -n 's/^.*protocol=\([^&]*\).*$/\1/p')

echo "$accio el switch $nom $ip"


echo "$(/usr/local/LosChichos/system/nc_client "switchs configurar $accio $nom $ip $user $pass $protocol" 2>&1) <br>"


/bin/cat <<EOM
</body>
</html>
EOM
