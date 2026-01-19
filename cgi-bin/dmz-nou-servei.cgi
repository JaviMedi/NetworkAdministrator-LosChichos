#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf


echo "Content-type: text/html; charset=utf-8"
echo ""

echo "<html><head><title>Crear VLAN</title>"
echo "<meta charset='utf-8'>"
 
cat $DIR/$PROJECTO/$DIR_CGI/$CSS_CGI_BIN
 
echo "</head><body>"

echo "<h2>Obrir nou servei</h2>"
echo "<form action='/cgi-bin/dmz-agregar.cgi' method='get'>"
echo "<table>"
echo "<tr><th>Port</th><th>Protocol</th><th>IP servidor</th></tr>"
echo "<tr>"
# port
echo "<td><input type='text' name='port' value='' style='width: 250px;'></td>"
# protocol
echo "<td><input type='text' name='proto' value='' ></td>"
# IP més amplis
echo "<td><input type='text' class='ipdmz' name='ipdmz' value=''></td>"
echo "</tr>"
echo "</table>"
echo "<button type='submit'>Obrir</button>"
echo "</form>"

echo "</body></html>"

