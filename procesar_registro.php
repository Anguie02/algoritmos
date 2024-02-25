<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title></title>
  <style>
    body {
      background-color: #f4f4f4;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }

    #resultado-container {
      background-color: #fff;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      padding: 20px;
      text-align: center;
    }
  </style>
</head>
<body>

<div id="resultado-container">
  <?php
    //código PHP para procesar el formulario y mostrar el mensaje
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Obtener los valores del formulario
        $nombres = $_POST["nombres"];
        $apellidos = $_POST["apellidos"];
        $dni = $_POST["dni"];
        $correo = $_POST["correo"];
        $celular = $_POST["celular"];
        $contrasena = $_POST["contrasena"];

        // Hash de la contraseña
        $hash_contrasena = password_hash($contrasena, PASSWORD_DEFAULT);

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

        // Consulta preparada para insertar los datos en la base de datos
        $stmt = $conn->prepare("INSERT INTO clientes (nombres, apellidos, dni, correo, celular, contrasena) VALUES (?, ?, ?, ?, ?, ?)");
        $stmt->bind_param("ssssss", $nombres, $apellidos, $dni, $correo, $celular, $hash_contrasena);

        if ($stmt->execute()) {
            echo "<p>Registro exitoso</p>";
        } else {
            echo "<p>Error al registrar: " . $stmt->error . "</p>";
        }

        // Cerrar la conexión a la base de datos
        $stmt->close();
        $conn->close();
    }
  ?>
</div>

</body>
</html>