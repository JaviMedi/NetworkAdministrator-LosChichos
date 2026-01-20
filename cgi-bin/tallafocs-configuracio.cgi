#!/bin/bash


source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Hola món CGI</title>
<style>
body {
  font-family: Arial, sans-serif;
  background-color: #f6f6f6;
  color: #333;
  margin: 20px;
}
h2 {
  background-color: #003366;
  color: white;
  padding: 10px;
  border-radius: 5px;
}
table {
  border-collapse: collapse;
  width: 60%;
  background: white;
  box-shadow: 0 0 5px rgba(0,0,0,0.2);
}
td, th {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}
th {
  background-color: #e9edf2;
}
input[type=text] {
  width: 95%;
  padding: 5px;
  border: 1px solid #aaa;
  border-radius: 3px;
}
button {
  padding: 8px 15px;
  background-color: #003366;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #0055aa;
}
.status-green {
  color: green;
  font-weight: bold;
}

.status-red {
  color: red;
  font-weight: bold;
}

.status-yellow {
  color: yellow;
  font-weight: bold;
}
</style>
</head>
<body>
EOM

for linia in $(grep -v '#' "$DIR/$PROJECTO/$DIR_CONF/$BRIDGE_CONF"); do
	    nom=$(echo "$linia"|cut -d';' -f1)
	    id=$(echo "$linia"|cut -d';' -f2)
	    ip=$(echo "$linia"|cut -d';' -f3)
	    #estat_vlan=$("$DIR"/"$PROJECTE"/"$DIR_SCRIPTS"/client_srv_cli tallafocs estat $id)
		estat_vlan=$(cd /usr/local/LosChichos/scripts/ && ./tallafocs estat $id)
	    if [ $estat_vlan == "CONNECTADA" ]; then
		  	echo "<h2>  $nom $ip <span class='status-green'>$estat_vlan</span></h2>"
	    	echo "<a href='tallafocs-conndeconn.cgi?id=$id&accio=desconnectar'><button type='button'>DESCONECTAR</button></a>"
        echo "<a href='tallafocs-aislar.cgi?id=$id&accio=aislar'><button type='button'>AISLAR</button></a>"
	    elif [ $estat_vlan == "DESCONNECTADA" ]; then
			  echo "<h2>  $nom $ip <span class='status-red'>$estat_vlan</span></h2>"
	     	echo "<a href='tallafocs-conndeconn.cgi?id=$id&accio=connectar'><button type='button'>CONNECTAR</button></a>"
			  echo "<a href='tallafocs-conndeconn.cgi?id=$id&accio=connectar_port_wls'><button type='button'>CONNECTAR WLS PUERTOS</button></a>"
		  elif [ $estat_vlan == "CONNECTADA-PORTS-WLS" ]; then
			  echo "<h2>  $nom $ip <span class='status-yellow'>$estat_vlan</span></h2>"
	    	echo "<a href='tallafocs-conndeconn.cgi?id=$id&accio=desconnectar'><button type='button'>DESCONECTAR</button></a>"
        echo "<a href='tallafocs-conndeconn.cgi?id=$id&accio=connectar'><button type='button'>CONNECTAR SIN RESTRICCIONES</button></a>"
      elif [[ "$estat_vlan" == "CONNECTADA-AISLADA" ]]; then
        echo "<h2>  $nom $ip <span class='status-yellow'>$estat_vlan</span></h2>"
        echo "<a href='tallafocs-conndeconn.cgi?id=$id&accio=desconnectar'><button type='button'>DESCONECTAR</button></a>"
        echo "<a href='tallafocs-aislar.cgi?id=$id&accio=desaislar'><button type='button'>DESAISLAR</button></a>"
		  else 
			echo "<h2>  $nom $ip <span class='status-yellow'>$estat_vlan</span></h2>"
	    fi
	  
	    
done
echo "<br>"
echo "<br>"
echo "<h2> </h2>" 
echo "<br>"
echo "<h2> WHITELIST PUERTOS</h2>" 
/bin/cat << EOM

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
  <thead>
    <tr>
      <th>Protocol</th>
      <th>Port</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
EOM

#Ports WLS

for linia in $(grep -v '#' "$DIR/$PROJECTO/$DIR_CONF/$PORTS_WLS"); do
	    PROTOCOL=$(echo "$linia"|cut -d';' -f1)
	    PORT=$(echo "$linia"|cut -d';' -f2) 
	    echo "<tr>"
	    echo "<td>$PROTOCOL</td>"
	    echo "<td>$PORT</td>"
	    echo "<td>"
	    echo "<a href='tallafocs-ports-wls.cgi?accio=eliminar_port_wls&protocol=$PROTOCOL&port=$PORT'><button type='button'>Eliminar</button></a>"
	    echo "</td>"
	    echo "</tr>"	   
done
echo "</tbody>"
echo "</table>"
echo "<a href='tallafocs-nova-port-wls.cgi?'><button type='button'>Añadir puerto</button></a>"

echo "<br>"
echo "<br>"
echo "<h2> </h2>" 
echo "<br>"
echo "<h2> IPS CON ACCESO SIN RESTRINGIR</h2>" 
/bin/cat << EOM

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
  <thead>
    <tr>
      <th>vid</th>
      <th>ip</th>
      <th>mac</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
EOM

for linia in $(grep -v '#' "$DIR/$PROJECTO/$DIR_CONF/$IPS_WLS"); do
	    VID=$(echo "$linia"|cut -d';' -f1)
	    IP=$(echo "$linia"|cut -d';' -f2) 
	    MAC=$(echo "$linia"|cut -d';' -f3) 
	    echo "<tr>"
	    echo "<td>$VID</td>"
	    echo "<td>$IP</td>"
	    echo "<td>$MAC</td>"
	    echo "<td>"
	    echo "<a href='tallafocs-ips-wls.cgi?accio=eliminar_ip_wls&vid=$VID&ip=$IP&mac=$MAC'><button type='button'>Eliminar</button></a>"
	    echo "</td>"
	    echo "</tr>"	   
done
echo "</tbody>"
echo "</table>"
echo "<a href='tallafocs-nova-ip-wls.cgi?'><button type='button'>Añadir ip</button></a>"
#echo "<button onclick=\"location.href='/cgi-bin/tallafocs-nova-ip-wls.cgi?'\">Añadir ip</button>"

/bin/cat << EOM
</body>
</html>
EOM


