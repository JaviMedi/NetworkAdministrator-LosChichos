#!/bin/bash

echo "Content-type: text/html; charset=utf-8"
echo ""

/bin/cat << EOM
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ebtables - Menú</title>
  <style type="text/css">
<!--
.estado {
	font-size: 18px;
	font-style: normal;
	color: #e9ab17;
	font-weight: bold;
	font-family: Georgia, "Times New Roman", Times, serif;
}
.cabecera {
	font-family: Verdana, Arial, Helvetica, sans-serif;
	color: #2A5B45;
}
.Estilo1 {color: #FF00FF}
.Estilo2 {color: #000000}
-->
h4{
  background: #f2f6fa;
  border-left: 5px solid #003366;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
}
h4:hover {
  background: #d0e4f5;
  cursor: pointer;
  border-left-color: #0055aa;
}
h4:active {
  background: #a6c8e0;
  border-left-color: #002244;
}
h4 a {
  text-decoration: none;
  color: #003366;
  display: block; 
}
h4 a:hover {
  color: #001f3f;
}
</style>
</head>
<body>

<h4><a href="ebtables.cgi?comand=iniciar" target="body">Ebtables Start</a></h4>
<h4><a href="ebtables.cgi?comand=aturar" target="body">Ebtables Stop</a></h4>
<h4><a href="ebtables.cgi?comand=restart" target="body">Ebtables Restart</a></h4>
<h4><a href="ebtables.cgi?comand=estat" target="body">Ebtables Status</a></h4>

<hr>

<h4><a href="ebtables-config.cgi" target="body">Configurar VLANs</a></h4>

</body>
</html>
EOM
