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

echo "<h2>$comand</h2>"
case "$comand" in
	"iniciar")
		echo "<pre>$(/usr/local/LosChichos/system/nc_client "dhcp iniciar") </pre> <br>"
		;;
	"aturar")
		echo "<pre>$(/usr/local/LosChichos/system/nc_client "dhcp aturar") </pre> <br>"
		;;
	"configurar")
		accio=$(echo "$QUERY_STRING" | sed -n 's/^.*accio=\([^&]*\).*$/\1/p')
		case "$accio" in
			"guardar_conf")
				vid=$(echo "$QUERY_STRING" | sed -n 's/^.*vid=\([^&]*\).*$/\1/p')
				inici=$(echo "$QUERY_STRING" | sed -n 's/^.*inici=\([^&]*\).*$/\1/p')
				final=$(echo "$QUERY_STRING" | sed -n 's/^.*final=\([^&]*\).*$/\1/p')
				gateway=$(echo "$QUERY_STRING" | sed -n 's/^.*gateway=\([^&]*\).*$/\1/p')
				dns1=$(echo "$QUERY_STRING" | sed -n 's/^.*dns1=\([^&]*\).*$/\1/p')
				activat=$(echo "$QUERY_STRING" | sed -n 's/^.*activat=\([^&]*\).*$/\1/p')
				echo "$(/usr/local/LosChichos/system/nc_client "dhcp configurar guardar_conf $vid $inici $final $gateway $dns1 $activat") <br>"
				;;
			"guardar_wifi_conf")
				ip=$(echo "$QUERY_STRING" | sed -n 's/^.*ip=\([^&]*\).*$/\1/p')
				ip=$(printf '%b' "${ip//%/\\x}")
				inici=$(echo "$QUERY_STRING" | sed -n 's/^.*inici=\([^&]*\).*$/\1/p')
				final=$(echo "$QUERY_STRING" | sed -n 's/^.*final=\([^&]*\).*$/\1/p')
				gateway=$(echo "$QUERY_STRING" | sed -n 's/^.*gateway=\([^&]*\).*$/\1/p')
				dns1=$(echo "$QUERY_STRING" | sed -n 's/^.*dns1=\([^&]*\).*$/\1/p')
				activat=$(echo "$QUERY_STRING" | sed -n 's/^.*activat=\([^&]*\).*$/\1/p')
				echo "$(/usr/local/LosChichos/system/nc_client "dhcp configurar guardar_wifi_conf $ip $inici $final $gateway $dns1 $activat") <br>"
				;;
			*)
				echo "falta [guardar_conf, guardar_wifi_conf]"
				;;
		esac
		;;
	"estat")
    echo "<pre>$(/usr/local/LosChichos/system/nc_client "dhcp estat") </pre>"
		;;
	*)
		echo "falta [iniciar, aturar, configurar, estat]"
		;;
esac


/bin/cat <<EOM
</body>
</html>
EOM
