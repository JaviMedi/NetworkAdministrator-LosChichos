#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat <<EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
  <style>
    pre {
      background: white;
      padding: 20px;
      border: 1px solid #ccc;
      box-shadow: 0 0 5px rgba(0,0,0,0.2);
      white-space: pre-wrap;
      font-family: monospace;
    }
  </style>
</head>
<body>
EOM

comand=$(echo "$QUERY_STRING" | sed -n 's/^.*comand=\([^&]*\).*$/\1/p')

echo "<h2>Configuración Wifi</h2>"
echo "<pre>"
case "$comand" in
	"iniciar")
		/usr/local/LosChichos/system/nc_client "wifi iniciar" 2>&1
		;;
	"aturar")
		/usr/local/LosChichos/system/nc_client "wifi aturar" 2>&1
		;;
	"guardar")
		interface=$(echo "$QUERY_STRING" | sed -n 's/^.*interface=\([^&]*\).*$/\1/p')
		ip=$(echo "$QUERY_STRING" | sed -n 's/^.*ip=\([^&]*\).*$/\1/p')
		ip=$(printf '%b' "${ip//%/\\x}")
		driver=$(echo "$QUERY_STRING" | sed -n 's/^.*driver=\([^&]*\).*$/\1/p')
		ssid=$(echo "$QUERY_STRING" | sed -n 's/^.*wifi_ssid=\([^&]*\).*$/\1/p')
		hw_mode=$(echo "$QUERY_STRING" | sed -n 's/^.*hw_mode=\([^&]*\).*$/\1/p')
		channel=$(echo "$QUERY_STRING" | sed -n 's/^.*channel=\([^&]*\).*$/\1/p')
		auth_algs=$(echo "$QUERY_STRING" | sed -n 's/^.*auth_algs=\([^&]*\).*$/\1/p')
		ignore_broadcast_ssid=$(echo "$QUERY_STRING" | sed -n 's/^.*ignore_broadcast_ssid=\([^&]*\).*$/\1/p')
		ap_isolate=$(echo "$QUERY_STRING" | sed -n 's/^.*ap_isolate=\([^&]*\).*$/\1/p')
		wpa=$(echo "$QUERY_STRING" | sed -n 's/^.*wpa=\([^&]*\).*$/\1/p')
		wpa_passphrase=$(echo "$QUERY_STRING" | sed -n 's/^.*wpa_passphrase=\([^&]*\).*$/\1/p')
		wpa_key_mgmt=$(echo "$QUERY_STRING" | sed -n 's/^.*wpa_key_mgmt=\([^&]*\).*$/\1/p')
		rsn_pairwise=$(echo "$QUERY_STRING" | sed -n 's/^.*rsn_pairwise=\([^&]*\).*$/\1/p')
		/usr/local/LosChichos/system/nc_client "wifi configurar guardar_wifi_ip $ip" 2>&1
		/usr/local/LosChichos/system/nc_client "wifi configurar guardar_wifi_hostapd_conf $interface $driver $ssid $hw_mode $channel $auth_algs $ignore_broadcast_ssid $ap_isolate $wpa $wpa_passphrase $wpa_key_mgmt $rsn_pairwise" 2>&1
		;;
	"estat")
		/usr/local/LosChichos/system/nc_client "wifi estat" 2>&1
		;;
esac
echo "</pre>"


/bin/cat <<EOM
</body>
</html>
EOM
