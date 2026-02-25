#!/bin/bash
source /usr/local/LosChichos/system/auth.lib

# Lee la cookie para obtener el token actual
cookie_header="$HTTP_COOKIE"
token=$(echo "$cookie_header" | grep -o "session_token=[^;]*" | cut -d= -f2)

if [ -n "$token" ]; then
    # Eliminar el archivo de sesión si existe
    session_file="$SESSION_DIR/$token"
    if [ -f "$session_file" ]; then
        rm -f "$session_file"
    fi
fi

# Eliminar la cookie en el navegador pidiendo que expire en el pasado
echo "Set-Cookie: session_token=; HttpOnly; SameSite=Strict; Path=/cgi-bin/; expires=Thu, 01 Jan 1970 00:00:00 GMT"
echo "Status: 302 Found"
echo "Location: /cgi-bin/login.cgi"
echo ""
exit 0
