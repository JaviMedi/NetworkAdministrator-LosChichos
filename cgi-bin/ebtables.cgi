#!/bin/bash

# Dispatcher script similar to tallafocs.cgi
# Handles: comand=start|iniciar|stop|aturar|estat|status

echo "Content-type: text/html; charset=utf-8"
echo ""

# Get command parameter
comand=$(echo "$QUERY_STRING" | sed -n 's/^.*comand=\([^&]*\).*$/\1/p')

/bin/cat << EOM
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ebtables Command</title>
EOM
cat /usr/local/LosChichos/cgi-bin/css.txt
/bin/cat << EOM
    <style>
        pre {
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
    <h2>Ejecutando: $comand</h2>
    <pre>
EOM

if [ -n "$comand" ]; then

    
    REAL_CMD="$comand"
    case "$comand" in
        iniciar) REAL_CMD="start" ;;
        aturar) REAL_CMD="stop" ;;
        estat) REAL_CMD="status" ;;
    esac

    /usr/local/LosChichos/system/nc_client "ebtables $REAL_CMD"
else
    echo "Error: No se especificó comando."
fi

/bin/cat << EOM
    </pre>
</body>
</html>
EOM
