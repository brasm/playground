<?php
$i=explode(" ",fgets(STDIN));
$r=array();
$t = array_shift($i);
$c = array($t);
foreach($i as $n){
    if( $n != $t+1){
        $r[] = $c;
        $c = array($n);
    }
    else {
        $c[1] = $n;
    }
    $t = $n;
}
$r[] = $c;
$s = array();
foreach($r as $x)
    $s[] = implode($x,"-");
echo trim(implode($s,', ')).".";
