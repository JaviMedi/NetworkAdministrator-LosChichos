#!/bin/bash


source /usr/local/LosChicos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="1; url=/cgi-bin/tallafocs-configuracio.cgi">
  <title>Hola món CGI</title>
</head>
<body>
EOM

accio=$(echo "$QUERY_STRING" | sed -n 's/^.*accio=\([^&]*\).*$/\1/p')
id=$(echo "$QUERY_STRING" | sed -n 's/^.*id=\([^&]*\).*$/\1/p')


#echo "<pre>$("$DIR"/"$PROJECTE"/"$DIR_SCRIPTS"/client_srv_cli tallafocs configurar $accio $id) </pre><br>"
{
  echo "tallafocs configurar $accio $id"
  echo "exit"
} | nc 127.0.0.1 1234 | sed 's/LosChichos>//g'


/bin/cat << EOM
</body>
</html>
EOM


