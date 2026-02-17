#!/bin/bash

echo "Content-type: text/html; charset=utf-8"
echo ""

# Parse Query String
# Expects: action=...&id=...
# Simplistic parsing
action=$(echo "$QUERY_STRING" | sed -n 's/^.*action=\([^&]*\).*$/\1/p')
id=$(echo "$QUERY_STRING" | sed -n 's/^.*id=\([^&]*\).*$/\1/p')

# Determine Command
CMD=""
REDIRECT="ebtables-info.cgi"

case "$action" in
    start|iniciar)
        CMD="ebtables start"
        REDIRECT="ebtables-info.cgi"
        ;;
    stop|aturar)
        CMD="ebtables stop"
        REDIRECT="ebtables-info.cgi"
        ;;
    restart)
        CMD="ebtables restart"
        REDIRECT="ebtables-info.cgi"
        ;;
    aislar)
        if [ -n "$id" ]; then
            CMD="ebtables conf aislar $id"
            REDIRECT="ebtables-config.cgi"
        fi
        ;;
    desaislar)
        if [ -n "$id" ]; then
            CMD="ebtables conf desaislar $id"
            REDIRECT="ebtables-config.cgi"
        fi
        ;;
esac

/bin/cat << EOM
<html>
<head>
  <meta charset="utf-8">
  <title>Ebtables Exec</title>
  <meta http-equiv="refresh" content="2; url=$REDIRECT">
EOM
cat /usr/local/LosChichos/cgi-bin/css.txt
/bin/cat << EOM
  <style>
    body { text-align: center; }
    .processing { margin-top: 50px; }
    pre {
        text-align: left;
        background: white;
        padding: 20px;
        border: 1px solid #ccc;
        box-shadow: 0 0 5px rgba(0,0,0,0.2);
        max-width: 800px;
        margin: 20px auto;
        white-space: pre-wrap;
    }
  </style>
</head>
<body>
    <div class="processing">
        <h2>Procesando acción: $action ${id:+($id)}...</h2>
        <pre>
EOM

if [ -n "$CMD" ]; then
    # Execute via socket service (root)
    # The srv_cli expects "script_name args..."
    # So "ebtables aislar 1" -> script=ebtables, args=aislar, 1
    # We pipe "ebtables aislar 1" to nc
    /usr/local/LosChichos/system/nc_client "$CMD"
else
    echo "Error: Acción no válida o faltan parámetros."
fi

/bin/cat << EOM
        </pre>
        <p>Redirigiendo...</p>
    </div>
</body>
</html>
EOM
