<?php 
function v($n,$w=1){
    $s="$n bottle".($n>1?"s":"")." of beer";
    return $w ? $s. " on the wall" : $s;
}
for($i=99;$i>0;$i--){
    $a="Take one down and pass it around, ".v($i-1);
    $z="Go to the store and buy some more, ".v(99);
    printf("%s, %s.\n%s.\n\n",v($i),v($i,0),$i>1?$a:$z);
}

