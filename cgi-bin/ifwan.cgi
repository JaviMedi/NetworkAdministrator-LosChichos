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

QUERY_STRING_DECODED=$(echo "$QUERY_STRING" | sed 's/+/ /g; s/%/\\x/g' | xargs -0 printf "%b")

comand=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*comand=\([^&]*\).*/\1/p')
mode=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*mode=\([^&]*\).*/\1/p')
interfaz=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*interface=\([^&]*\).*/\1/p')
ipmask=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*ipmask=\([^&]*\).*/\1/p')
gtw=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*gtw=\([^&]*\).*/\1/p')
dns=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*dns=\([^&]*\).*/\1/p')

echo "<h2>Configuración WAN</h2>"

echo "<pre>"
{
  echo "ifwan $comand $mode $interfaz $ipmask $gtw $dns"
  echo "exit"
} | stdbuf -oL nc 127.0.0.1 1234 | sed -u 's/LosChichos>//g' 



/bin/cat << EOM
</pre>
</body>
</html>
