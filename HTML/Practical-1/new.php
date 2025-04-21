<?php
$sum = 5;
for($i=1;$i < $sum; $i++); { 
    $fac=1;
    for($j=1; $j < $i; $j++) { 
        $fac *= $j;
    }
    echo "The Factorial of $i is : $fac <br>"; 
}
?>