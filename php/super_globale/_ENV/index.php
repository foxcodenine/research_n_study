<?php 

// $_ENV — Environment variables


putenv("USER=Fred");
echo getenv("USER") . "\n\n";


$_ENV["USER"] = $_ENV["USER"] ?? 'James';

echo $_ENV["USER"]  . "\n\n";
print_r($_ENV);
