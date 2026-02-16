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
body {
  font-family: Arial, sans-serif;
  background-color: #f6f6f6;
  color: #333;
  margin: 20px;
}
h2 {
  background-color: #003366;
  color: white;
  padding: 10px;
  border-radius: 5px;
}
table {
  border-collapse: collapse;
  width: 60%;
  background: white;
  box-shadow: 0 0 5px rgba(0,0,0,0.2);
}
td, th {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}
th {
  background-color: #e9edf2;
}
input[type=text] {
  width: 95%;
  padding: 5px;
  border: 1px solid #aaa;
  border-radius: 3px;
}
button {
  padding: 8px 15px;
  background-color: #003366;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #0055aa;
}
.status-green {
  color: green;
  font-weight: bold;
}

.status-red {
  color: red;
  font-weight: bold;
}

.status-yellow {
  color: yellow;
  font-weight: bold;
}
</style>
</head>
<body>
EOM

while IFS= read -r linia; do

    nom=$(echo "$linia" | cut -d';' -f1 | tr -d '"')
    id=$(echo "$linia" | cut -d';' -f2 | tr -d '"')
    ip=$(echo "$linia" | cut -d';' -f3 | tr -d '"')

    estat_switch=$(cd /usr/local/LosChichos/scripts/ && ./switch status "$id")

    if [ "$estat_switch" == "$ACTIVADO" ]; then
        echo "<h2>$nom $ip <span class='status-green'>$estat_switch</span></h2>"
    elif [ "$estat_switch" == "$DESACTIVADO" ]; then
        echo "<h2>$nom $ip <span class='status-red'>$estat_switch</span></h2>"
    else 
        echo "<h2>$nom $ip <span class='status-yellow'>$estat_switch</span></h2>"
    fi

done < <(grep -v '^#' "$DIR/$PROJECTO/$DIR_CONF/$SWITCH_CONF")

echo "<div style='margin-top: 20px;'>"
echo "<button onclick=\"window.location.href='/cgi-bin/switch-configurar.cgi'\">Añadir</button>"
echo "<button onclick=\"window.location.href='/cgi-bin/switch-eliminar.cgi'\">Eliminar</button>"
echo "</div>"
echo "</body></html>"