#!/bin/bash
source /usr/local/LosChichos/system/auth.lib

if [ "$REQUEST_METHOD" = "POST" ]; then
    read -n $CONTENT_LENGTH POST_DATA
    USERNAME=$(echo "$POST_DATA" | grep -o "username=[^&]*" | cut -d= -f2)
    PASSWORD=$(echo "$POST_DATA" | grep -o "password=[^&]*" | cut -d= -f2)

    USERNAME=$(echo -e "${USERNAME//%/\\x}")
    PASSWORD=$(echo -e "${PASSWORD//%/\\x}")

    if check_credentials "$USERNAME" "$PASSWORD"; then
        TOKEN=$(create_session "$USERNAME")
        echo "Set-Cookie: session_token=$TOKEN; HttpOnly; SameSite=Strict; Path=/cgi-bin/"
        echo "Status: 302 Found"
        echo "Location: /cgi-bin/main.cgi"
        echo ""
        exit 0
    else
        ERROR_MSG="Usuario o contraseña incorrectos"
    fi
fi

echo "Content-type: text/html; charset=UTF-8"
echo ""
cat << EOF
<!DOCTYPE html>
<html>
<head>
<title>Login - LosChichos</title>
<style>
body { font-family: Arial, sans-serif; background-color: #f6f6f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
.login-box { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); width: 300px; }
h2 { text-align: center; color: #333; }
input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
button { width: 100%; padding: 10px; background-color: #003366; color: white; border: none; border-radius: 4px; cursor: pointer; }
button:hover { background-color: #002244; }
.error { color: red; text-align: center; font-size: 0.9em; }
</style>
</head>
<body>
<div class="login-box">
    <h2>Iniciar Sesión</h2>
    ${ERROR_MSG:+<p class="error">$ERROR_MSG</p>}
    <form method="POST" action="/cgi-bin/login.cgi">
        <input type="text" name="username" placeholder="Usuario" required>
        <input type="password" name="password" placeholder="Contraseña" required>
        <button type="submit">Entrar</button>
    </form>
</div>
</body>
</html>
EOF
