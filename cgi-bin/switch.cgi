#!/bin/bash
echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Switch CGI</title>
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
nombre=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*nombre=\([^&]*\).*/\1/p')
id=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*id=\([^&]*\).*/\1/p')
ip=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*ip=\([^&]*\).*/\1/p')
redirect=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*redirect=\([^&]*\).*/\1/p')


echo "<h2>Configuración SWITCH</h2>"
echo "<pre>"

if [ -n "$redirect" ]; then

    if [ "$comand" == "añadir_switch" ]; then
         {
            echo "switch $comand \"$nombre\" \"$id\" \"$ip\""
            echo "exit"
        } | stdbuf -oL nc 127.0.0.1 1234 >/dev/null 2>&1
    elif [ "$comand" == "eliminar_switch" ]; then
         {
            echo "switch $comand \"$id\""
            echo "exit"
        } | stdbuf -oL nc 127.0.0.1 1234 >/dev/null 2>&1
    else
         # Fallback for other commands if any
         {
            echo "switch $comand"
            echo "exit"
        } | stdbuf -oL nc 127.0.0.1 1234 >/dev/null 2>&1
    fi
    
    echo "<script>
          setTimeout(function(){
            window.location.href='/$redirect';
          }, 200);
          </script>"

else
    # Direct command
    {
      echo "switch $comand"
      echo "exit"
    } | stdbuf -oL nc 127.0.0.1 1234 | sed -u 's/LosChichos>//g'
fi

echo "</pre>"
echo "</body></html>"
