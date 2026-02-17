#!/bin/bash
echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
    <style>
body {
  font-family: Arial, sans-serif;
  background-color: #eef3f8;
  color: #333;
  margin: 0;
  padding: 0;
}
.header {
  background-color: #003366;
  color: white;
  padding: 15px;
  text-align: center;
  font-size: 1.5em;
  font-weight: bold;
}
h3 {
  background: #f2f6fa;
  border-left: 5px solid #003366;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
}
  </style>
</head>
<body>
EOM

comand=$(echo "$QUERY_STRING" | sed -n 's/^.*comand=\([^&]*\).*$/\1/p')


echo "<h3>Configuración ENRUTAMIENTO</h3><br><b>"

#expect /usr/local/LosChichos/scripts/exp_model
{
  #echo "enrutar $comand"
  #echo "exit"
  /usr/local/LosChichos/system/nc_client "enrutar $comand"
}
#echo "$(/usr/local/LosChichos/system/client_srv_cli enrutar $comand) <br>"
echo "</b>"

/bin/cat << EOM
</body>
</html>
EOM

