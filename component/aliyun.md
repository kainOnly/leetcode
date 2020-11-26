## 阿里云相关扩展

阿里云相关扩展是针对阿里云库的统一简化，首先使用 `composer` 安装操作服务

```shell
composer require kain/think-aliyun-extra
```

安装后服务将自动注册，然后需要更新配置 config/aliyun.php，例如：

```php
return [

    'accessKeyId' => env('aliyun.id'),
    'accessKeySecret' => env('aliyun.secret'),
    'oss' => [
        'endpoint' => env('aliyun.oss_endpoint'),
        'extranet' => env('aliyun.oss_extranet'),
        'bucket' => env('aliyun.oss_bucket')
    ]

];
```

- **accessKeyId** `string` 阿里云 keyid
- **accessKeySecret** `string` 阿里云 key secret
- **oss**
  - **endpoint** `string` 对象存储endpoint
  - **extranet** `string` 对象存储外网地址
  - **bucket** `string` 桶名

### Oss::getClient(bool $extranet = false): OssClient

获取对象存储客户端

### Oss::put(string $name): string

上传至阿里云对象存储

- **name** `string` File 请求文件
- **Return** `string` 对象名称

```php
use think\support\facade\Oss;

public function uploads()
{
    try {
        $saveName = Oss::put('image');
        return [
            'error' => 0,
            'data' => [
                'savename' => $saveName,
            ]
        ];
    } catch (\Exception $e) {
        return [
            'error' => 1,
            'msg' => $e->getMessage()
        ];
    }
}
```