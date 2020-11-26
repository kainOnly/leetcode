## 华为云相关扩展

华为云相关扩展是针对华为云库的统一简化，首先使用 `composer` 安装操作服务

```shell
composer require kain/think-huaweicloud-extra
```

安装后服务将自动注册，然后需要更新配置 config/huaweicloud.php，例如：

```php
return [

    'accessKeyId' => env('huaweicloud.id'),
    'accessKeySecret' => env('huaweicloud.secret'),
    'obs' => [
        'endpoint' => env('huaweicloud.obs_endpoint'),
        'bucket' => env('huaweicloud.obs_bucket')
    ]

];
```

- **accessKeyId** `string` 华为云 keyid
- **accessKeySecret** `string` 华为云 key secret
- **obs**
  - **endpoint** `string` 对象存储endpoint
  - **bucket** `string` 桶名

### Obs::getClient(): ObsClient

获取对象存储客户端

### Obs::put(string $name): string

上传至华为云对象存储

- **name** `string` File 请求文件
- **Return** `string` 对象名称

```php
use think\support\facade\Obs;

public function uploads()
{
    try {
        $saveName = Obs::put('image');
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