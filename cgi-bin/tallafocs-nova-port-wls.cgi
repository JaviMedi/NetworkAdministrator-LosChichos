#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf


echo "Content-type: text/html; charset=utf-8"
echo ""

echo "<html><head><title>Crear VLAN</title>"
echo "<meta charset='utf-8'>"
 

cat $DIR/$PROJECTO/$DIR_CGI/$CSS_CGI_BIN

echo "</head><body>"

echo "<h2>Añadir puerto a whitelist</h2>"
echo "<form action='/cgi-bin/tallafocs-ports-wls.cgi' method='get'>"
echo "<input type='hidden' name='accio' value='afegir_port_wls'>"
echo "<table>"
echo "<tr><th>protocolo</th><th>puerto</th></tr>"
echo "<tr>"
echo "<td><input type='text' name='protocol' value='' style='width: 250px;'></td>"
echo "<td><input type='text' name='port' value='' ></td>"
echo "</tr>"
echo "</table>"
echo "<button type='submit'>Añadir</button>"
echo "</form>"

echo "</body></html>"
