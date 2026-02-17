#!/bin/bash

# Configuration
SECURE_DIR="/usr/local/LosChichos/seguro"
USER_DB="$SECURE_DIR/usuarios.db"

# Ensure secure directory exists
if [ ! -d "$SECURE_DIR" ]; then
    mkdir -p "$SECURE_DIR"
    chmod 700 "$SECURE_DIR"
    chown root:www-data "$SECURE_DIR"
fi

# Ensure database exists
if [ ! -f "$USER_DB" ]; then
    touch "$USER_DB"
    chmod 600 "$USER_DB"
    chown root:www-data "$USER_DB"
fi

function show_help {
    echo "Uso: $0 {add|del|list} [username]"
    exit 1
}

function add_user {
    username="$1"
    if [ -z "$username" ]; then
        echo "Error: Debes especificar un nombre de usuario."
        exit 1
    fi

    # Check if user exists
    if grep -q "^$username:" "$USER_DB"; then
        echo "Error: El usuario '$username' ya existe."
        exit 1
    fi

    echo -n "Introduce contraseña: "
    read -s password
    echo
    echo -n "Confirma contraseña: "
    read -s password_confirm
    echo

    if [ "$password" != "$password_confirm" ]; then
        echo "Error: Las contraseñas no coinciden."
        exit 1
    fi

    # Genera hash (SHA-512)
    hash=$(openssl passwd -6 "$password")
    
    # Guarda en la base de datos
    echo "$username:$hash" >> "$USER_DB"
    echo "Usuario '$username' añadido correctamente."
}

function del_user {
    username="$1"
    if [ -z "$username" ]; then
        echo "Error: Debes especificar un nombre de usuario."
        exit 1
    fi

    if ! grep -q "^$username:" "$USER_DB"; then
        echo "Error: El usuario '$username' no existe."
        exit 1
    fi

    # Remove user
    grep -v "^$username:" "$USER_DB" > "$USER_DB.tmp" && mv "$USER_DB.tmp" "$USER_DB"
    chmod 600 "$USER_DB"
    echo "Usuario '$username' eliminado correctamente."
}

function list_users {
    echo "Usuarios registrados:"
    cut -d: -f1 "$USER_DB"
}

# Main logic
case "$1" in
    add)
        add_user "$2"
        ;;
    del)
        del_user "$2"
        ;;
    list)
        list_users
        ;;
    *)
        show_help
        ;;
esac
