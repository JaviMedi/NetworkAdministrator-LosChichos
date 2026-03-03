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
cat $DIR/$PROJECTO$DIR_CGI/$CSS_CGI_BIN
/bin/cat <<EOM

</head>
<body>
<h2>Switchs</h2>

<h4><a href="/cgi-bin/switchs-estat.cgi" target="body">Estado Switchs</a></h4>
<h4><a href="/cgi-bin/switchs-estat-acls.cgi" target="body">Estado ACLs</a></h4>
<h4><a href="/cgi-bin/switchs.cgi?accio=iniciar" target="body">Iniciar todas las ACLs</a></h4>
<h4><a href="/cgi-bin/switchs.cgi?accio=aturar" target="body">Parar todas las ACLs</a></h4>
<h4><a href="/cgi-bin/switchs-taules-macs.cgi?comand=totes_les_taula_mac&" target="body">Mostrar Tablas MACs</a></h4>
<h4><a href="/cgi-bin/switchs-macs-vlans.cgi?accio=veure_macs_blocades&" target="body">MACs bloqueadas en todos los puertos</a></h4>
<h4><a href="/cgi-bin/switchs-macs-admin.cgi?accio=veure_macs_vlan_admin&" target="body">MACs administradas en VLAN ADMIN</a></h4>
</body>
</html>

EOM
