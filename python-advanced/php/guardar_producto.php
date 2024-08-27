<?php
// Conexión a la base de datos
$conn = new mysqli("localhost", "root", "", "clientes_db");

// Verificar la conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Obtener los datos del formulario
$nombre = $_POST['nombre'];
$cantidad = $_POST['cantidad'];
$valorventa = $_POST['valorventa'];
$proveedor = $_POST['proveedor'];


// Insertar los datos en la tabla clientes
$sql = "INSERT INTO productos (nombre, cantidad, valorventa, proveedor)
        VALUES ('$nombre', '$cantidad', '$valorventa', '$proveedor')";

if ($conn->query($sql) === TRUE) {
    echo "Nuevo producto registrado exitosamente.";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Cerrar la conexión
$conn->close();
?>