<?php
// $_SERVER — Server and execution environment information

// _____________________________________________________________________

if (php_sapi_name() == 'cli-server') {

foreach($_SERVER as $k => $v) {
    echo $k . ' => ' . $v . '<br/><br/>';
}

/*
DOCUMENT_ROOT   => /home/foxcodenine/git/repo/research_n_study/php/super_globale
PHP_SELF        => /$_SERVER/index.php
SCRIPT_NAME     => /$_SERVER/index.php
SCRIPT_FILENAME => /home/foxcodenine/git/repo/research_n_study/php/super_globale/$_SERVER/index.php
REQUEST_URI     => /$_SERVER/index.php?name=chris&surname=farrugia
QUERY_STRING    => name=chris&surname=farrugia
*/

/*
HTTP_HOST       => localhost:3000
REQUEST_METHOD  => GET

SERVER_NAME     => localhost
SERVER_PORT     => 3000

SERVER_SOFTWARE => PHP 8.0.8 Development Server
SERVER_PROTOCOL => HTTP/1.1

REMOTE_ADDR     => 127.0.0.1
REMOTE_PORT     => 40044

*/

/*
argv    => Array ([0] => index.php)
argc    => 1
*/

}


// _____________________________________________________________________

if (php_sapi_name() == "cli") {


// In cli-mode

print('$_SERVER[\'argv\'] :');
print_r($_SERVER['argv']);
print("\n");

print('$_SERVER[\'argc\'] :');
print_r($_SERVER['argc']);
print("\n");


}
?>