#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat <<EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
EOM
cat $DIR/$PROJECTO$DIR_CGI/$CSS_CGI_BIN
/bin/cat <<EOM
</head>
<body>
EOM


echo "<h2> LISTA SWITCHS</h2>"

/bin/cat <<EOM

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
  <thead>
    <tr>
      <th>nombre</th>
      <th>ip</th>
      <th>estado</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
EOM

while IFS=' ' read -r nom ip estat; do
   	echo "<tr>"
	echo "<td>$nom</td>"
	if [[ "$estat" == "FUNCIONA" ]]; then
		echo "<td><a href='http://$ip'>$ip</a></td>"
		echo "<td class='status-green'>$estat</td>"
	else
		echo "<td>$ip</td>"
		echo "<td class='status-red'>$estat</td>"
	fi
	echo "<td>"
	echo "<a href='switchs-configurar.cgi?accio=eliminar_switch&nom=$nom&ip=$ip'><button type='button'>Eliminar</button></a>"
	echo "</td>"
	echo "</tr>"
done < <( /usr/local/LosChichos/system/nc_client "switchs estat" 2>&1 )
	
echo "</tbody>"
echo "</table>"
echo "<button onclick=\"location.href='/cgi-bin/switchs-nou.cgi'\">Agregar nuevo switch</button>"
echo "</body></html>"
