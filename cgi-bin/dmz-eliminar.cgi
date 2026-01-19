#!/bin/bash


source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
EOM
cat $DIR/$PROJECTO/$DIR_CGI/$CSS_CGI_BIN
/bin/cat << EOM
</head>
<body>
EOM

PORT=$(echo "$QUERY_STRING" | sed -n 's/^.*port=\([^&]*\).*$/\1/p')
PROTO=$(echo "$QUERY_STRING" | sed -n 's/^.*proto=\([^&]*\).*$/\1/p')
IP_DMZ=$(echo "$QUERY_STRING" | sed -n 's/^.*ipdmz=\([^&]*\).*$/\1/p')

echo "<h2>ELIMINAR $PORT $PROTO $IP_DMZ</h2>" 
echo "<pre>"

{
  echo "dmz configurar eliminar $PORT $PROTO $IP_DMZ"
  echo "exit"
} | nc 127.0.0.1 1234 | sed 's/LosChichos>//g'
echo "</pre><br>>"


/bin/cat << EOM
</body>
</html>
EOM

