#!/bin/bash
echo "Content-type: text/html"
echo ""

source /usr/local/LosChichos/conf/variables.conf

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
<h4><a href="/cgi-bin/wifi.cgi?comand=iniciar&" target="body">Wifi Start</a></h4>
<h4><a href="/cgi-bin/wifi.cgi?comand=aturar&" target="body">Wifi Stop</a></h4>
<h4><a href="/cgi-bin/wifi.cgi?comand=estat&" target="body">Wifi Status</a></h4>
<h4><a href="/cgi-bin/wifi-configuracio.cgi" target="body">Wifi Config</a></h4>
</body>
</html>

EOM
