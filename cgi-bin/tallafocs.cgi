#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf


echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
  <style>
body { font-family: sans-serif; margin: 20px; background: #f6f6f6; }
h2 { background: #ddd; padding: 6px; }
table { border-collapse: collapse; margin-bottom: 20px; width: 80%; }
td, th { border: 1px solid #999; padding: 6px 10px; text-align: left; }
th { background: #f0f0f0; }
button { padding: 4px 10px; margin-left: 5px; }
</style>
</head>
<body>
EOM

comand=$(echo "$QUERY_STRING" | sed -n 's/^.*comand=\([^&]*\).*$/\1/p')



#echo "<pre>$("$DIR"/"$PROJECTE"/"$DIR_SCRIPTS"/client_srv_cli tallafocs $comand) </pre><br>"


{
  echo "tallafocs $comand"
  echo "exit"
}  | stdbuf -oL nc 127.0.0.1 1234 | sed -u 's/LosChichos>//g' | while IFS= read -r line; do
    printf '%s<br>\n' "$line"
    # Forzar vaciado de salida HTML
    perl -e 'select STDOUT; $|=1;'
done 


/bin/cat << EOM
</body>
</html>
EOM
