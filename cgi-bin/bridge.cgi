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
v_b=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*v_b=\([^&]*\).*/\1/p')
nombre=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*nombre=\([^&]*\).*/\1/p')
vid=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*vid=\([^&]*\).*/\1/p')
subnet=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*subnet=\([^&]*\).*/\1/p')
gw=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*gw=\([^&]*\).*/\1/p')
redirect=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*redirect=\([^&]*\).*/\1/p')
enp=$(echo "$QUERY_STRING" | sed -n 's/^.*enp=\([^&]*\).*$/\1/p')
raw_tag=$(echo "$QUERY_STRING" | sed -n 's/^.*tag=\([^&]*\).*$/\1/p')
  tag=$(printf '%b' "${raw_tag//%/\\x}")
raw_untag=$(echo "$QUERY_STRING" | sed -n 's/^.*untag=\([^&]*\).*$/\1/p')
  untag=$(printf '%b' "${raw_untag//%/\\x}")


echo "<h2>Configuración BRIDGE</h2>"



echo "<pre>"
# Esto es para redirigir de nuevo a la página de configuración tras hacer la acción y que no se muestre la salida del comando por pantalla 
# (solo para páginas con redirect)
if [ -n "$redirect" ]; then

  if [ -n "$enp" ]; then
     /usr/local/LosChichos/system/nc_client "bridge $comand $mode $v_b $enp $untag $tag" >/dev/null 2>&1
    echo "<script>
          setTimeout(function(){
            window.location.href='/$redirect';
          }, 200);
          </script>"

  else
    /usr/local/LosChichos/system/nc_client "bridge $comand $mode $v_b $nombre $vid $subnet $gw" >/dev/null 2>&1
    echo "<script>
          setTimeout(function(){
            window.location.href='/$redirect';
          }, 200);
          </script>"
  fi

else # Si no hay redirect, mostramos la salida del comando, para el start, stop y status
  /usr/local/LosChichos/system/nc_client "bridge $comand $mode $v_b $nombre $vid $subnet $gw"
fi
echo "</pre>"


/bin/cat << EOM
</body>
</html>
EOM

