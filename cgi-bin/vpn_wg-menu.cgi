#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf
echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat <<EOM

<html>
<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta content="MSHTML 6.00.2900.3660" name=GENERATOR> 

EOM
cat $DIR/$PROJECTO/$DIR_CGI/$CSS_CGI_BIN
/bin/cat <<EOM

</head>
<body>
<h2>VPN WireGuard</h2>

<h4><a href="/cgi-bin/vpn_wg.cgi?comand=iniciar&" target="body">iniciar</a></h4>
<h4><a href="/cgi-bin/vpn_wg.cgi?comand=aturar&" target="body">aturar</a></h4>
<h4><a href="/cgi-bin/vpn_wg.cgi?comand=estat&" target="body">estat</a></h4>
<h4><a href="/cgi-bin/vpn_wg-configuracio.cgi" target="body">configuracio</a></h4>
</body>
</html>

EOM
