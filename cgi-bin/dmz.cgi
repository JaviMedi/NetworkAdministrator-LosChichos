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
cat $DIR/$PROJECTE/$DIR_CGI/$CSS_CGI_BIN
/bin/cat << EOM
</head>
<body>
EOM

comand=$(echo "$QUERY_STRING" | sed -n 's/^.*comand=\([^&]*\).*$/\1/p')

echo "<h2>$comand</h2>" 
echo "<pre>$("$DIR"/"$PROJECTE"/"$DIR_SCRIPTS"/client_srv_cli dmz $comand) </pre><br>"
if [[ "$comand" != "estat" ]] then
	echo "<pre>$("$DIR"/"$PROJECTE"/"$DIR_SCRIPTS"/client_srv_cli dmz estat) </pre><br>"
fi

{
  echo "dmz $comand"
  if [[ "$comand" != "estat" ]] then
    echo "dmz estat"
  fi
  echo "exit"
} | stdbuf -oL nc 127.0.0.1 1234 | sed -u 's/LosChichos>//g' | while IFS= read -r line; do
    printf '%s<br>\n' "$line"
    # Forzar vaciado de salida HTML
    perl -e 'select STDOUT; $|=1;'
done 


/bin/cat << EOM
</body>
</html>
EOM

