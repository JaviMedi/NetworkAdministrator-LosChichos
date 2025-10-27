#!/bin/bash
echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
</head>
<body>
EOM

comand=$(echo "$QUERY_STRING" | sed -n 's/^.*comand=\([^&]*\).*$/\1/p')

echo "Configuració ENRUTAMENT <br>"

#expect /usr/local/LosChichos/scripts/exp_model
{
  echo "enrutar $comand"
  echo "exit"
} | nc 127.0.0.1 1234 | sed 's/LosChichos>//g'
#echo "$(/usr/local/LosChichos/system/client_srv_cli enrutar $comand) <br>"


/bin/cat << EOM
</body>
</html>
EOM

