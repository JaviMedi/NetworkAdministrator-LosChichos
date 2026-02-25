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

echo "<h2>Configuración DMZ</h2>"
echo "<pre>"
/usr/local/LosChichos/system/nc_client "dmz $comand" 2>&1
if [[ "$comand" != "estat" ]]; then
	echo ""
	/usr/local/LosChichos/system/nc_client "dmz estat" 2>&1
fi
echo "</pre>"


/bin/cat << EOM
</body>
</html>
EOM

