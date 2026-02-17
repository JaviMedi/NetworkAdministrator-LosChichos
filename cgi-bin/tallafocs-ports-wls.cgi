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
EOM
cat $DIR/$PROJECTO/$DIR_CGI/$CSS_CGI_BIN
/bin/cat << EOM
</head>
<body>
EOM

accio=eliminar_ip_wls&vid=$VIP&ip=$IP&mac=$MAC

accio=$(echo "$QUERY_STRING" | sed -n 's/^.*accio=\([^&]*\).*$/\1/p')
protocol=$(echo "$QUERY_STRING" | sed -n 's/^.*protocol=\([^&]*\).*$/\1/p')
port=$(echo "$QUERY_STRING" | sed -n 's/^.*port=\([^&]*\).*$/\1/p')


#echo "<pre>$("$DIR"/"$PROJECTE"/"$DIR_SCRIPTS"/client_srv_cli tallafocs configurar $accio $protocol $port )  </pre><br>"
echo "<pre>" 
  /usr/local/LosChichos/system/nc_client "tallafocs configurar $accio $protocol $port"
echo "</pre>"

/bin/cat << EOM
</body>
</html>
EOM



