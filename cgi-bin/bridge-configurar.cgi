#!/bin/bash

source /usr/local/LosChichos/conf/variables.conf


echo "Content-type: text/html; charset=utf-8"
echo ""

echo "<html><head><title>Gestió de VLANs</title>"
echo "<meta charset='utf-8'>"
echo "<style>
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
</style>
</style>"
echo "</head><body>"

# -------------------------------------------------------------------
# Aquí posem la comanda o fitxer que genera les VLANs
# -------------------------------------------------------------------
VLAN_DATA=$(cd "$DIR"/"$PROJECTO"/"$DIR_SCRIPTS"/ && ./bridge conf show vlan)



# Llegim totes les línies en un array
mapfile -t VLANS <<< "$VLAN_DATA"

# Comprovem que tinguem almenys dues línies
if [ "${#VLANS[@]}" -lt 2 ]; then
    echo "<p><b>Error:</b> no hi ha prou VLANs definides.</p>"
    echo "</body></html>"
    exit 0
fi

# -------------------------------------------------------------------
# VLAN ADMINISTRACIÓ (primera línia)
# -------------------------------------------------------------------
echo "<h2>VLAN ADMINISTRACIÓ</h2>"
echo "<table>"
echo "<tr><th>Nom</th><th>VID</th><th>Subxarxa</th><th>Gateway</th><th>Accions</th></tr>"
IFS=';' read -r nom vid subnet gw _ <<< "${VLANS[0]}"
echo "<tr><td>$nom</td><td>$vid</td><td>$subnet</td><td>$gw</td>"
echo "<td><button onclick=\"location.href='/cgi-bin/bridge-modificar.cgi?vid=$vid'\">Modificar</button></td></tr>"
echo "</table>"

# -------------------------------------------------------------------
# VLAN DMZ (segona línia)
# -------------------------------------------------------------------
echo "<h2>VLAN DMZ</h2>"
echo "<table>"
echo "<tr><th>Nom</th><th>VID</th><th>Subxarxa</th><th>Gateway</th><th>Accions</th></tr>"
IFS=';' read -r nom vid subnet gw _ <<< "${VLANS[1]}"
echo "<tr><td>$nom</td><td>$vid</td><td>$subnet</td><td>$gw</td>"
echo "<td><button onclick=\"location.href='/cgi-bin/bridge-modificar.cgi?vid=$vid'\">Modificar</button></td></tr>"
echo "</table>"

# -------------------------------------------------------------------
# Altres VLANS (de la tercera en avant)
# -------------------------------------------------------------------
echo "<h2>VLANS</h2>"
echo "<table>"
echo "<tr><th>Nom</th><th>VID</th><th>Subxarxa</th><th>Gateway</th><th>Accions</th></tr>"

for ((i=2; i<${#VLANS[@]}; i++)); do
    line="${VLANS[$i]}"
    [ -z "$line" ] && continue
    IFS=';' read -r nom vid subnet gw _ <<< "$line"
    echo "<tr><td>$nom</td><td>$vid</td><td>$subnet</td><td>$gw</td>"
    echo "<td>"
    echo "<button onclick=\"location.href='/cgi-bin/bridge-modificar.cgi?vid=$vid'\">Modificar</button>"
    echo "<button onclick=\"location.href='/cgi-bin/bridge-esborrar.cgi?vid=$vid'\">Esborrar</button>"
    echo "</td></tr>"
done

echo "</table>"

# -------------------------------------------------------------------
# Botó final
# -------------------------------------------------------------------
echo "<button onclick=\"location.href='/cgi-bin/bridge-nova-vlan.cgi'\">Crear nova VLAN</button>"

echo "</body></html>"
