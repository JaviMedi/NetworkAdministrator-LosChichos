#!/bin/bash
source /usr/local/LosChichos/conf/variables.conf

echo "Content-type: text/html"
echo ""

estado_ifwan() {
  cd $DIR/$PROJECTO/$DIR_SCRIPTS/ && ./ifwan status
}

estado_enrutar() {
  cd $DIR/$PROJECTO/$DIR_SCRIPTS/ && ./enrutar status | tail -n +2 
}

estado_bridge() {
   cd $DIR/$PROJECTO/$DIR_SCRIPTS/ && ./bridge status | head -n 1
}

estado_firewall() {
    if sudo iptables -L ports_wls >/dev/null 2>&1; then
        echo "ACTIVADO"
    else
        echo "DESACTIVADO"
    fi
}


pintar_estado() {
#  estado="$1"
estado="$(echo "$1" | head -n 1)"
    if [ "$estado" = "ACTIVADO" ]; then
        echo "<span class='status-green'>ACTIVADO</span>"
    elif [ "$estado" = "DESACTIVADO" ]; then
        echo "<span class='status-red'>DESACTIVADO</span>"
    else
        echo "<span class='status-yellow'>DESCONOCIDO</span>"
    fi
}


cat << EOF
<html>
<head>
<title>Estado de servicios</title>

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
  margin-bottom: 30px;
}
td, th {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: left;
}
th {
  color: #003366;
  background-color: #e9edf2;
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
  color: orange;
  font-weight: bold;
}
</style>
</head>

<body>

<h2>ESTADO SCRIPTS</h2>
<table>
<tr><th>Servicio</th><th>Estado</th></tr>
<tr>
  <td>Conexion</td>
  <td>$(pintar_estado "$(estado_ifwan)")</td>
</tr>
<tr>
  <td>Enrutamiento</td>
  <td>$(pintar_estado "$(estado_enrutar)")</td>
</tr>
<tr>
  <td>Bridge</td>
  <td>$(pintar_estado "$(estado_bridge)")</td>
</tr>
<tr>
  <td>Firewall</td>
  <td>$(pintar_estado "$(estado_firewall)")</td>
</tr>
</table>


</body>
</html>
EOF
