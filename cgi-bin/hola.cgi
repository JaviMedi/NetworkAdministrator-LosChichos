#!/bin/bash
echo "Content-type: text/html"
echo ""

cat << 'EOF'
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Panel de Configuración - Bienvenida</title>
<style>
body {
  font-family: Arial, sans-serif;
  background-color: #eef3f8;
  color: #333;
  margin: 0;
  padding: 0;
}
.header {
  background-color: #003366;
  color: white;
  padding: 15px;
  text-align: center;
  font-size: 1.5em;
  font-weight: bold;
}
.container {
  margin: 40px auto;
  width: 80%;
  max-width: 700px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0px 2px 8px rgba(0,0,0,0.2);
  padding: 25px 30px;
}
h2 {
  color: #003366;
}
ul {
  list-style: none;
  padding-left: 0;
}
ul li {
  background: #f2f6fa;
  border-left: 5px solid #003366;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
}
.footer {
  text-align: center;
  font-size: 0.9em;
  color: #666;
  margin-top: 40px;
}
</style>
</head>
<body>
<div class="header">Panel de Configuración del Servidor</div>

<div class="container">
  <h2>Bienvenido</h2>
  <p>Este panel le permite gestionar y monitorizar distintos aspectos de tu red</p>

  <ul>
    <li><strong>Red:</strong> Configuración de interfaces, estado de conexiones WAN/LAN.</li>
    <li><strong>Sistema:</strong> Control de servicios, procesos y tareas automáticas.</li>
    <li><strong>Accesos:</strong> Administración de cuentas y permisos de acceso.</li>
    <li><strong>Logs:</strong> Consulta de registros del sistema y diagnósticos.</li>
  </ul>

  <p>Seleccione una opción del menú lateral o superior para comenzar la configuración.</p>
</div>


</body>
</html>
EOF
