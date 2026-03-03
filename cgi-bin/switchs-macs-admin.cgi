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

if [ "$accio" == "veure_macs_vlan_admin" ]; then
	RESULTAT=$(/usr/local/LosChichos/system/nc_client "switchs configurar $accio" 2>&1)
  
  #echo "Estat blocatge "
  #echo "<a href='/cgi-bin/switchs-aplicar-blocar-mac.cgi?accio=blocar&'>Aplica Blocar</a>"
  #echo "<a href='/cgi-bin/switchs-aplicar-blocar-mac.cgi?accio=desblocar&'>No Aplica Blocar</a>"

  echo "</tbody></table>"
	echo "<br>"
	echo "<h2>Tabla de macs admitidas en vlan admin</h2>"
	echo "<table>"
	echo "<thead><tr><th>MAC</th><th></th></tr></thead>"
	echo "<tbody>"	
	while IFS= read -r linia; do
    if [ -z "$linia" ]; then
      continue
    fi
		echo "<tr><td>$linia</td><td><a href='/cgi-bin/switchs-macs-admin.cgi?accio=eliminar_mac_vlan_admin&mac=$linia'><button type="button">Eliminar</button></a></td></tr>"
	done <<< "$RESULTAT"
	echo "</tbody></table>"
  
  echo "<br>"
  echo "<h2>Agregar mac</h2>"
  echo "<table>"
  echo "<thead><tr><th>MAC</th><th></th></tr></thead>"
  echo "<tbody>"
  echo "<form action='/cgi-bin/switchs-macs-admin.cgi' method='get'>"
  echo "<input type='hidden' value='afegir_mac_vlan_admin' name='accio'>"
  echo "<tr><td><input type='text' name='mac'></td>"
  echo "<td><input type='submit' value='Agregar i aplicar'></td></tr>"
  echo "</form>"
  echo "</tbody></table>"

elif [ "$accio" == "eliminar_mac_vlan_admin" ]; then
 echo "Eliminar mac vlan admin"
  mac=$(echo "$QUERY_STRING" | sed -n 's/^.*mac=\([^&]*\).*$/\1/p'| sed 's/%3[aA]/:/g')
	RESULTAT=$(/usr/local/LosChichos/system/nc_client "switchs configurar eliminar_mac_vlan_admin $mac" 2>&1)
  echo "$RESULTAT"

elif [ "$accio" == "afegir_mac_vlan_admin" ]; then
 echo "Agregar mac vlan admin"
  mac=$(echo "$QUERY_STRING" | sed -n 's/^.*mac=\([^&]*\).*$/\1/p'| sed 's/%3[aA]/:/g')
	RESULTAT=$(/usr/local/LosChichos/system/nc_client "switchs configurar afegir_mac_vlan_admin $mac" 2>&1)
  echo "$RESULTAT"
fi


echo "</body>"
echo "</html>"
