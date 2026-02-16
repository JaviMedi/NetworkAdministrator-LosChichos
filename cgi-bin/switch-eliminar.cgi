#!/bin/bash

# Configuration
source /usr/local/LosChichos/conf/variables.conf


echo "Content-type: text/html; charset=utf-8"
echo ""

echo "<html><head><title>Eliminar Switch</title>"
echo "<meta charset='utf-8'>"
echo "
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
</style>"
echo "</head><body>"

echo "<h2>Eliminar Switch</h2>"
echo "<form action='/cgi-bin/switch.cgi' method='get'>"
echo "<input type='hidden' name='comand' value='eliminar_switch'>"
echo "<input type='hidden' name='redirect' value='cgi-bin/switch-status.cgi'>"
echo "<table>"
echo "<tr><th>ID del Switch a eliminar</th></tr>"
echo "<tr>"
echo "<td><input type='text' name='id' value='' required placeholder='Introduzca el ID del switch'></td>"
echo "</tr>"
echo "</table>"
echo "<br>"
echo "<button type='submit'>Eliminar</button>"
echo "</form>"
echo "</body></html>"
