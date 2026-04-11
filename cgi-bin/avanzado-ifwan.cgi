#!/bin/bash

# Configuration and sourcing
source /usr/local/LosChichos/conf/variables.conf
echo "Content-type: text/html; charset=utf-8"
echo ""

# Parse Query Strings
QUERY_STRING_DECODED=$(echo "$QUERY_STRING" | sed 's/+/ /g; s/%/\\x/g' | xargs -0 printf "%b")

subcmd=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*subcmd=\([^&]*\).*/\1/p')
iface_req=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*interface=\([^&]*\).*/\1/p')
action=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*action=\([^&]*\).*/\1/p')
val=$(echo "$QUERY_STRING_DECODED" | sed -n 's/.*val=\([^&]*\).*/\1/p')

if [ -n "$subcmd" ] && [ -n "$iface_req" ] && [ -n "$action" ]; then
    # Validate and execute action
    /usr/local/LosChichos/system/nc_client "ifwan advanced $subcmd $iface_req $action $val" > /dev/null
    sleep 0.5
fi

cat << "EOM"
<html>
<head>
  <meta charset="utf-8">
  <title>Configuración Avanzada ifwan</title>
  <style>
    body { font-family: Arial, sans-serif; background-color: #eef3f8; color: #333; margin: 0; padding: 20px; }
    .header { background-color: #003366; color: white; padding: 15px; text-align: center; font-size: 1.5em; font-weight: bold; border-radius: 5px; margin-bottom: 20px;}
    .card { background: white; padding: 15px; border-radius: 8px; box-shadow: 0px 4px 8px rgba(0,0,0,0.1); margin-bottom: 20px; }
    h3 { color: #003366; border-bottom: 2px solid #003366; padding-bottom: 5px; margin-top: 0; }
    .status-badge { display: inline-block; padding: 5px 10px; border-radius: 12px; font-weight: bold; color: white; font-size: 0.9em; margin-left: 10px; }
    .up { background-color: #28a745; }
    .down { background-color: #dc3545; }
    .btn { padding: 8px 15px; border: none; border-radius: 5px; color: white; font-weight: bold; cursor: pointer; transition: 0.2s; margin-left:5px;}
    .btn-primary { background-color: #007bff; }
    .btn-primary:hover { background-color: #0056b3; }
    .btn-danger { background-color: #dc3545; }
    .btn-danger:hover { background-color: #c82333; }
    .btn-success { background-color: #28a745; }
    .btn-success:hover { background-color: #218838; }
    .form-group { margin-bottom: 15px; display: flex; align-items: center; }
    .form-group label { width: 120px; font-weight: bold; }
    .form-group input[type="text"] { flex: 1; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
  </style>
</head>
<body>
<div class="header">Configurador Avanzado de Tarjetas de Red</div>
<p>Todos los cambios realizados en esta página serán persistentes a reinicio</p>
EOM

global_gw_val=$(/usr/local/LosChichos/system/nc_client "ifwan advanced gw global status" | tr -d '\r\n')
global_dns_val=$(/usr/local/LosChichos/system/nc_client "ifwan advanced dns global status" | tr -d '\r\n')

cat << EOM
<div class="card" style="border: 2px solid #003366;">
  <h3>Configuración Global</h3>
  
  <!-- Gateway Form -->
  <form action="/cgi-bin/avanzado-ifwan.cgi" method="get">
    <div class="form-group">
      <label>Gateway Global:</label>
      <input type="hidden" name="subcmd" value="gw">
      <input type="hidden" name="interface" value="global">
      <input type="hidden" id="action_gw_global" name="action" value="">
      <input type="text" name="val" value="$global_gw_val" placeholder="Ej: 192.168.1.1">
      <button type="submit" class="btn btn-primary" onclick="document.getElementById('action_gw_global').value='add'">Aplicar GW</button>
      <button type="submit" class="btn btn-danger" onclick="document.getElementById('action_gw_global').value='del'">Borrar GW</button>
    </div>
  </form>

  <!-- DNS Form -->
  <form action="/cgi-bin/avanzado-ifwan.cgi" method="get">
    <div class="form-group">
      <label>DNS Global:</label>
      <input type="hidden" name="subcmd" value="dns">
      <input type="hidden" name="interface" value="global">
      <input type="hidden" id="action_dns_global" name="action" value="">
      <input type="text" name="val" value="$global_dns_val" placeholder="Ej: 8.8.8.8">
      <button type="submit" class="btn btn-primary" onclick="document.getElementById('action_dns_global').value='add'">Aplicar DNS</button>
      <button type="submit" class="btn btn-danger" onclick="document.getElementById('action_dns_global').value='del'">Borrar DNS</button>
    </div>
  </form>
</div>
EOM

for iface in $(ls /sys/class/net); do
  if [[ "$iface" == "lo" || "$iface" == br* ]]; then
    continue
  fi

  # Replace the carriage return and new lines from nc_client response securely
  estado=$(/usr/local/LosChichos/system/nc_client "ifwan advanced enp $iface status" | tr -d '\r\n')
  ip_val=$(/usr/local/LosChichos/system/nc_client "ifwan advanced ip $iface status" | tr -d '\r\n')


  badge_class="down"
  if [ "$estado" == "UP" ]; then
    badge_class="up"
  fi

  cat << EOM
<div class="card">
  <h3>Interfaz: $iface <span class="status-badge $badge_class">$estado</span></h3>
  
  <div style="margin-bottom: 20px;">
    <strong>Cambiar Estado:</strong>
    <form action="/cgi-bin/avanzado-ifwan.cgi" method="get" style="display:inline;">
      <input type="hidden" name="subcmd" value="enp">
      <input type="hidden" name="interface" value="$iface">
      <button type="submit" name="action" value="up" class="btn btn-success">Habilitar (UP)</button>
      <button type="submit" name="action" value="down" class="btn btn-danger">Deshabilitar (DOWN)</button>
    </form>
  </div>

  <form action="/cgi-bin/avanzado-ifwan.cgi" method="get">
    <div class="form-group">
      <label>IP / Máscara:</label>
      <input type="hidden" name="subcmd" value="ip">
      <input type="hidden" name="interface" value="$iface">
      <input type="hidden" id="action_ip_$iface" name="action" value="">
      <input type="text" name="val" value="$ip_val" placeholder="Ej: 192.168.1.10/24">
      <button type="submit" class="btn btn-primary" onclick="document.getElementById('action_ip_$iface').value='add'">Aplicar IP</button>
      <button type="submit" class="btn btn-danger" onclick="document.getElementById('action_ip_$iface').value='del'">Borrar IP</button>
    </div>
  </form>
</div>
EOM

done

echo "</body></html>"
