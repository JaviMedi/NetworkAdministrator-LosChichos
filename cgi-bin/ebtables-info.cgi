#!/bin/bash

echo "Content-type: text/html; charset=utf-8"
echo ""

OUTPUT=$(/usr/local/LosChichos/scripts/ebtables status)

/bin/cat << EOM
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>EBTABLES - Status</title>
EOM
cat /usr/local/LosChichos/cgi-bin/css.txt
/bin/cat << EOM
    <style>
        .box {
            background: white;
            padding: 20px;
            border: 1px solid #ccc;
            box-shadow: 0 0 5px rgba(0,0,0,0.2);
            white-space: pre-wrap;
            font-family: monospace;
        }
    </style>
</head>
<body>
    <a href="ebtables-menu.cgi"><button type="button">⬅ Volver al Menú</button></a>
    <h2>Estado del Servicio Ebtables</h2>
    <div class="box">
$OUTPUT
    </div>
</body>
</html>
EOM
