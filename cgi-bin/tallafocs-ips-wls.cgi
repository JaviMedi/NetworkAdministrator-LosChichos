#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="1; url=/cgi-bin/tallafocs-configuracio.cgi">
  <title>Hola món CGI</title>
</head>
EOM
cat $DIR/$PROJECTO/$DIR_CGI/$CSS_CGI_BIN
/bin/cat << EOM
<body>
EOM

accio=eliminar_ip_wls&vid=$VIP&ip=$IP&mac=$MAC

accio=$(echo "$QUERY_STRING" | sed -n 's/^.*accio=\([^&]*\).*$/\1/p')
vid=$(echo "$QUERY_STRING" | sed -n 's/^.*vid=\([^&]*\).*$/\1/p')
ip=$(echo "$QUERY_STRING" | sed -n 's/^.*ip=\([^&]*\).*$/\1/p')
mac=$(echo "$QUERY_STRING" | sed -n 's/^.*mac=\([^&]*\).*$/\1/p')


#echo "<pre>$("$DIR"/"$PROJECTE"/"$DIR_SCRIPTS"/client_srv_cli tallafocs configurar $accio $vid $ip $mac)  </pre><br>"

{
  echo "tallafocs configurar $accio $vid $id $mac"
  echo "exit"
} | nc 127.0.0.1 1234 | sed 's/LosChichos>//g'


/bin/cat << EOM
</body>
</html>
EOM



