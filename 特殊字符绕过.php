<?php
function filter($num)
{
    $num=str_replace("0x","1",$num);
    $num=str_replace("0","1",$num);
    $num=str_replace(".","1",$num);
    $num=str_replace("e","1",$num);
    $num=str_replace("+","1",$num);
    return $num;
}
$flag='000000000000';
// for ($i=0; $i <=1000 ; $i++) 
// { 
//     $x=chr($i).'36';
//     if(is_numeric($x) and $x!=='36' and trim($x)!=='36' and filter($x)=='36')
//     {
//         echo $i.' '.chr($i).' '.urlencode($x)." true\n";
//     }
//     else
//     {
//         echo $i.' '.chr($i).' '.urlencode($x)." false\n";
//     }
// }
for ($i=0; $i <=1000 ; $i++) 
{
    $b=chr($i)."4444444";
    
    if(strlen($b)>5 and mb_ereg_match("111".substr($b,0,1),"1114") and substr($b,0,1)!=4)
    {
        echo $b."true\n";
    }
    else
    {
        echo $b."false\n";
    }
}
?>
