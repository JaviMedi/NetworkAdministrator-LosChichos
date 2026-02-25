#!/bin/bash
echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
    <style>
pre {
      background: white;
      padding: 20px;
      border: 1px solid #ccc;
      box-shadow: 0 0 5px rgba(0,0,0,0.2);
      white-space: pre-wrap;
      font-family: monospace;
    }
  </style>
</head>
<body>
EOM

comand=$(echo "$QUERY_STRING" | sed -n 's/^.*comand=\([^&]*\).*$/\1/p')


echo "<h2>Configuración ENRUTAMIENTO</h2>"
echo "<pre>"
#expect /usr/local/LosChichos/scripts/exp_model
{
  #echo "enrutar $comand"
  #echo "exit"
  /usr/local/LosChichos/system/nc_client "enrutar $comand"
}
#echo "$(/usr/local/LosChichos/system/client_srv_cli enrutar $comand) <br>"
echo "</pre>"

/bin/cat << EOM
</body>
</html>
EOM

