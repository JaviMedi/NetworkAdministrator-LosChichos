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
	    elif [ $estat_vlan == "DESCONNECTADA" ]; then
			echo "<h2>  $nom $ip <span class='status-red'>$estat_vlan</span></h2>"
	     	echo "<a href='tallafocs-conndeconn.cgi?id=$id&accio=connectar'><button type='button'>CONNECTAR</button></a>"
			echo "<a href='tallafocs-conndeconn.cgi?id=$id&accio=connectar_port_wls'><button type='button'>CONNECTAR PORTS WLS</button></a>"
		elif [ $estat_vlan == "CONNECTADA-PORTS-WLS" ]; then
			echo "<h2>  $nom $ip <span class='status-yellow'>$estat_vlan</span></h2>"
	    	echo "<a href='tallafocs-conndeconn.cgi?id=$id&accio=desconnectar'><button type='button'>DESCONECTAR</button></a>"
		else 
			echo "<h2>  $nom $ip <span class='status-yellow'>$estat_vlan</span></h2>"
	    fi
	    echo "<br>" 
	    
done


/bin/cat << EOM
</body>
</html>
EOM


