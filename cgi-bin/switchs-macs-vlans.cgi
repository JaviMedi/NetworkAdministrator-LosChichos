#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

echo "<html>"
echo "<head>"
echo "  <meta charset=\"utf-8\">"
echo "  <title>Hola món CGI</title>"

cat $DIR/$PROJECTO$DIR_CGI/$CSS_CGI_BIN

echo "</head>"
echo "<body>"
accio=$(echo "$QUERY_STRING" | sed -n 's/^.*accio=\([^&]*\).*$/\1/p')

if [ "$accio" == "veure_macs_blocades" ]; then
	RESULTAT=$(/usr/local/LosChichos/system/nc_client "switchs configurar $accio" 2>&1)
  
  echo "</tbody></table>"
	echo "<br>"
	echo "<h2>Tabla de MACs Bloqueadas</h2>"
	echo "<table>"
	echo "<thead><tr><th>MAC</th><th></th></tr></thead>"
	echo "<tbody>"	
	while IFS= read -r linia; do
      if [ -z "$linia" ]; then
        continue
      fi
			echo "<tr><td>$linia</td><td><a href='/cgi-bin/switchs-blocar-mac.cgi?accio=desblocar&mac=$linia'><button type="button">Desbloquear</button></a></td></tr>"
	done <<< "$RESULTAT"
  echo "</tbody></table>"
  
  echo "<br>"
  echo "<h2>Bloquear MAC</h2>"
  echo "<table>"
  echo "<thead><tr><th>MAC</th><th></th></tr></thead>"
  echo "<tbody>"
  echo "<form action='/cgi-bin/switchs-blocar-mac.cgi' method='get'>"
  echo "<input type='hidden' value='blocar' name='accio'>"
  echo "<tr><td><input type='text' name='mac'></td>"
  echo "<td><input type='submit' value='Bloquear y aplicar'></td></tr>"
  echo "</form>"
  echo "</tbody></table>"

elif [ "$accio" == "desblocar" ]; then
  mac=$(echo "$QUERY_STRING" | sed -n 's/^.*mac=\([^&]*\).*$/\1/p')
	RESULTAT=$(/usr/local/LosChichos/system/nc_client "switchs configurar desblocar_mac $mac" 2>&1)
  echo "$RESULTAT"
fi


echo "</body>"
echo "</html>"
