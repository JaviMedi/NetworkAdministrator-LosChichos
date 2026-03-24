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
cat $DIR/$PROJECTO/$DIR_CGI/$CSS_CGI_BIN
/bin/cat <<EOM
</head>
<body>
EOM

comand=$(echo "$QUERY_STRING" | sed -n 's/^.*comand=\([^&]*\).*$/\1/p')



case $comand in 
	"iniciar" | "aturar")
		echo "<h2>VPN $comand</h2>"
		echo "<pre>$(/usr/local/LosChichos/system/nc_client "vpn_wg $comand") </pre><br>" 
    	echo "<pre>$(/usr/local/LosChichos/system/nc_client "vpn_wg estat") </pre><br>"
		;;
	"mostrar")
		echo "<h2>VPN $comand</h2>"
		argument=$(echo "$QUERY_STRING" | sed -n 's/^.*argument=\([^&]*\).*$/\1/p')
		accio=$(echo "$QUERY_STRING" | sed -n 's/^.*accio=\([^&]*\).*$/\1/p')
		RESULTAT=$(/usr/local/LosChichos/system/nc_client "vpn_wg mostrar $accio $argument")
		echo "<pre>$RESULTAT</pre><br>"
		echo "<form method='post' action='/cgi-bin/descarrega_resultat.cgi'>"
		echo "<textarea name='resultat' style='display:none;'>$RESULTAT</textarea>"
		echo "<textarea name='fitxer' style='display:none;'>wg-$argument.conf</textarea>"
		echo "<input type='submit' value='Descarregar wg-$argument.conf'>"
		echo "</form>"
		;;
	"configurar")
		accio=$(echo "$QUERY_STRING" | sed -n 's/^.*accio=\([^&]*\).*$/\1/p')
		case $accio in 
			"afegir_router")				
				ip_publica=$(echo "$QUERY_STRING" | sed -n 's/^.*ip_publica=\([^&]*\).*$/\1/p')
				rutes=$(echo "$QUERY_STRING" | sed -n 's/^.*rutes=\([^&]*\).*$/\1/p')
				rutes=$(printf '%b' "${rutes//%/\\x}")
				echo "<h2>VPN $comand afegir router $ip_publica</h2>"
				echo "<pre>$(/usr/local/LosChichos/system/nc_client "vpn_wg configurar $accio $ip_publica $rutes") </pre><br>"
				echo "Router $ip_publica afegit correctament"
				;;
			"eliminar_router")
				ip_publica=$(echo "$QUERY_STRING" | sed -n 's/^.*ip_publica=\([^&]*\).*$/\1/p')
				echo "<h2>VPN $comand eliminar router $ip_publica</h2>"
				echo "<pre>$(/usr/local/LosChichos/system/nc_client "vpn_wg configurar $accio $ip_publica") </pre><br>"
				echo "Router $ip_publica eliminat correctament"
				;;
			"afegir_usuari")
				argument=$(echo "$QUERY_STRING" | sed -n 's/^.*argument=\([^&]*\).*$/\1/p')
				echo "<h2>VPN $comand afegir usuari $argument</h2>"
				echo "<pre>$(/usr/local/LosChichos/system/nc_client "vpn_wg configurar $accio $argument") </pre><br>"
				echo "Usuari $argument afegit correctament"
				;;
			"eliminar_usuari")
				argument=$(echo "$QUERY_STRING" | sed -n 's/^.*argument=\([^&]*\).*$/\1/p')
				echo "<h2>VPN $comand eliminar usuari $argument</h2>"
				echo "<pre>$(/usr/local/LosChichos/system/nc_client "vpn_wg configurar $accio $argument") </pre><br>"
				echo "Usuari $argument eliminat correctament"
				;;
		esac
		;;
	"estat")
		echo "<h2>VPN Estat</h2>"
		RESULTAT=$(/usr/local/LosChichos/system/nc_client "vpn_wg estat router")
		echo "<pre>$RESULTAT</pre>"
		if [[ $RESULTAT =~ ^$ACTIVADO ]]; then
			echo ""
			echo "<h4><a href=\"/cgi-bin/vpn_wg.cgi?comand=mostrar&argument=config_int_router\" target=\"body\">veure configuracio wg-routers</a></h4>"
		fi

		echo "<h3>  </h3>"
		
		RESULTAT=$(/usr/local/LosChichos/system/nc_client "vpn_wg estat users")
		echo "<pre>$RESULTAT</pre>"
		if [[ $RESULTAT =~ ^$ACTIVADO ]]; then
			echo ""
			echo "<h4><a href=\"/cgi-bin/vpn_wg.cgi?comand=mostrar&argument=config_int_usuari\" target=\"body\">veure configuracio wg-users</a></h4>"
		fi

		echo "<h3>  </h3>"
		;;
esac 

/bin/cat <<EOM
</body>
</html>
EOM
