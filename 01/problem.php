<?php

$floor = 0;
$position = 0;
$wasInTheBasement = false;

$fp = fopen("php://stdin", "r");
if(!$fp) {
    die('Error: Can\'t open file');
}

while (!feof($fp)) {
    $buffer = fgets($fp, 1024);

    $len = strlen($buffer);
    for($i = 0; $i < $len; $i++) {

        $position++;
        switch ($buffer[$i]) {

            case '(':
                $floor++;
                break;

            case ')':
                $floor--;
                break;

            default:
                break;
        }

        if($floor < 0 && !$wasInTheBasement) {
            echo 'First time in basement at position: ' . $position . PHP_EOL;
            $wasInTheBasement = true;
        }

    }
}

fclose($fp);

echo 'End floor: ' . $floor . PHP_EOL;
