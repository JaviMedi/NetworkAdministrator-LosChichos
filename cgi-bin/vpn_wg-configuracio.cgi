#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

echo "<html><head><title>Gestió de VPN WireGuard</title>"
echo "<meta charset='utf-8'>"

cat $DIR/$PROJECTO/$DIR_CGI/$CSS_CGI_BIN

echo "</head><body>"

ROUTERS_DATA="$(/usr/local/LosChichos/system/nc_client vpn_wg mostrar llista_routers)"

# Llegim totes les línies en un array
mapfile -t ROUTERS <<<"$ROUTERS_DATA"

# -------------------------------------------------------------------
# VPN WireGuard CONFIGURACIO ROUTERS
# -------------------------------------------------------------------
echo "<h2>VPN WireGuard CONFIGURACIO ROUTERS</h2>"
echo "<table>"
echo "<tr><th>IP PÚBLICA</th><th>IP PRIVADA</th><th>Rutes</th><th></th></tr>"

for ((i = 0; i < ${#ROUTERS[@]}; i++)); do
	line="${ROUTERS[$i]}"
	[ -z "$line" ] && continue
	IFS=';' read -r ip_publica ip_privada clau_publica clau_privada rutes <<<"$line"
	echo "<tr><td>$ip_publica</td><td>$ip_privada</td><td>$rutes</td>"
	echo "<td><button onclick=\"location.href='/cgi-bin/vpn_wg.cgi?comand=configurar&accio=eliminar_router&ip_publica=$ip_publica'\">Eliminar</button>"
	echo "<button onclick=\"location.href='/cgi-bin/vpn_wg.cgi?comand=mostrar&accio=config_router&argument=$ip_publica'\">Mostrar configuració</button></td>"
	echo "</tr>"
done

echo "</table>"

#echo "<h3>VPN WireGuard AFEGIR ROUTER</h3>"
echo "<form action='/cgi-bin/vpn_wg.cgi' method='get'>"
echo "<input type='hidden' name='accio' value='afegir_router'>"
echo "<input type='hidden' name='comand' value='configurar'>"
echo "<table>"
echo "<tr><th>ip publica</th><th>rutes</th><th></th></tr>"
echo "<tr><td><input type='text' name='ip_publica' placeholder='IP Publica'></td><td><input type='text' name='rutes' placeholder='Rutes'></td><td><input type='submit' value='Afegir'></td></tr>"
echo "</table>"
echo "</form>"


echo "<br>"
# -------------------------------------------------------------------
# VPN WireGuard CONFIGURACIO USUARIS
# -------------------------------------------------------------------

USUARIS_DATA="$(/usr/local/LosChichos/system/nc_client vpn_wg mostrar llista_usuaris)"

# Llegim totes les línies en un array
mapfile -t USUARIS <<<"$USUARIS_DATA"

echo "<h2>VPN WireGuard CONFIGURACIO USUARIS</h2>"
echo "<table>"
echo "<tr><th>nom d'usuari</th><th>ip privada</th><th></th></tr>"

for ((i = 0; i < ${#USUARIS[@]}; i++)); do
	line="${USUARIS[$i]}"
	[ -z "$line" ] && continue
	IFS=';' read -r usuari ip clau_publica clau_privada rutes<<<"$line"
	echo "<tr><td>$usuari</td><td>$ip</td>"
	echo "<td><button onclick=\"location.href='/cgi-bin/vpn_wg.cgi?accio=eliminar_usuari&comand=configurar&argument=$usuari'\">Eliminar</button>"
	echo "<button onclick=\"location.href='/cgi-bin/vpn_wg.cgi?comand=mostrar&accio=config_usuari&argument=$usuari'\">Mostrar configuració</button></td>"
	echo "</tr>"
done

echo "</table>"

#echo "<h4>VPN WireGuard AFEGIR USUARI</h4>"
echo "<form action='/cgi-bin/vpn_wg.cgi' method='get'>"
echo "<input type='hidden' name='accio' value='afegir_usuari'>"
echo "<input type='hidden' name='comand' value='configurar'>"
echo "<table>"
echo "<tr><th>nom d'usuari</th><th></th></tr>"
echo "<tr><td><input type='text' name='argument' placeholder='Usuari'></td><td><input type='submit' value='Afegir'></td></tr>"
echo "</table>"
echo "</form>"



echo "</body></html>"
