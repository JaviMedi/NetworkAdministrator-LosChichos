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

QUERY_STRING_DECODED=$(echo "$QUERY_STRING" | sed 's/+/ /g; s/%/\\x/g' | xargs -0 printf "%b")

comand=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*comand=\([^&]*\).*/\1/p')
mode=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*mode=\([^&]*\).*/\1/p')
interfaz=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*interface=\([^&]*\).*/\1/p')
ipmask=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*ipmask=\([^&]*\).*/\1/p')
gtw=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*gtw=\([^&]*\).*/\1/p')
dns=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*dns=\([^&]*\).*/\1/p')

echo "<h3>Configuració WAN</h3><br><b>"

#expect /usr/local/LosChichos/scripts/exp_model
{
  echo "ifwan $comand $mode $interfaz $ipmask $gtw $dns"
  echo "exit"
} | nc 127.0.0.1 1234 | sed 's/LosChichos>//g'
#echo "$(/usr/local/LosChichos/system/client_srv_cli enrutar $comand) <br>"


/bin/cat << EOM
</body>
</html>
EOM

