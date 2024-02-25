<?php
// Verificar si se ha enviado el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtener los valores del formulario
    $correo = $_POST["correo"];
    $contrasena_ingresada = $_POST["contrasena"];

    // Conectar a la base de datos 
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "tornillo_tienda";

    $conn = new mysqli($servername, $username, $password, $dbname);

    // Verificar la conexión
    if ($conn->connect_error) {
        die("Conexión fallida: " . $conn->connect_error);
    }

    // Consulta preparada para obtener la contraseña almacenada para el usuario
    $stmt = $conn->prepare("SELECT id_cliente, correo, contrasena FROM clientes WHERE correo = ?");
    $stmt->bind_param("s", $correo);
    $stmt->execute();
    $stmt->bind_result($id, $correo_bd, $contrasena_bd);
    $stmt->fetch();
    $stmt->close();

    // Verificar la autenticación
    if ($correo_bd && password_verify($contrasena_ingresada, $contrasena_bd)) {
        // Autenticación exitosa
        // Redirigir a otra página
        header("Location: otra_pagina.php");
        exit(); // Asegura que el script se detenga después de la redirección
    } else {
        // Autenticación fallida
        echo "Error: Usuario o contraseña incorrectos";
    }

    // Cerrar la conexión a la base de datos
    $conn->close();
}
?>