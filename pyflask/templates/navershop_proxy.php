<?php
header("Content-Type: text/html; charset=UTF-8");

require_once "navershopapi.php";

$food = new food();

echo $food->shopapi($_POST['query']);
?>