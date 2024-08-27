<?php
// Conexión a la base de datos
$conn = new mysqli("localhost", "root", "", "clientes_db");

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Obtener los datos del formulario
$nombre = $_POST['nombre'];
$correo = $_POST['correo'];
$telefono = $_POST['telefono'];
$direccion = $_POST['direccion'];
$ciudad = $_POST['ciudad'];
$pais = $_POST['pais'];

// Insertar los datos en la tabla clientes
$sql = "INSERT INTO clientes (nombre, correo, telefono, direccion, ciudad, pais)
        VALUES ('$nombre', '$correo', '$telefono', '$direccion', '$ciudad', '$pais')";

if ($conn->query($sql) === TRUE) {
    echo "Nuevo cliente registrado exitosamente.";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Cerrar la conexión
$conn->close();
?>