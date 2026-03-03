#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

echo "<html><head><title>Crear VLAN</title>"
echo "<meta charset='utf-8'>"

cat $DIR/$PROJECTO$DIR_CGI/$CSS_CGI_BIN

echo "</head><body>"

echo "<h2>Agregar nuevo switch</h2>"
echo "<form action='/cgi-bin/switchs-configurar.cgi' method='get'>"
echo "<input type='hidden' name='accio' value='afegir_switch' >"
echo "<table>"
echo "<tr><th>Nombre</th><th>IP</th><th>Usuario</th><th>Contraseña</th><th>Telnet|SSH</th></tr>"
echo "<tr>"
# Nom ara també més ample
echo "<td><input type='text' name='nom' value='' style='width: 250px;'></td>"
echo "<td><input type='text' name='ip' value='' ></td>"
echo "<td><input type='text' name='user' value=''></td>"
echo "<td><input type='text' name='pass' value=''></td>"
echo "<td><input type='text' name='protocol' value=''></td>"
echo "</tr>"
echo "</table>"
echo "<button type='submit'>Agregar switch</button>"
echo "</form>"

echo "</body></html>"
