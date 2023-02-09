<?php

if ($_POST) {
    $nombre = $_POST['tNombre'];
    $apellido = $_POST['tApellido'];
    echo "hola " . $nombre, $apellido;
}


?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="types_dates.php" method="post">
        <label for="1">Nombre</label>
        <input type="text" name="tNombre" id="1">
        <label for="2">Apellido</label>
        <input type="text" name="tApellido" id="2">
        <input type="submit" value="enviar">




    </form>
</body>

</html>