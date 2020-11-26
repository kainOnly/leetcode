## Auth 鉴权验证

AuthVerify 鉴权验证是一个抽象定义中间件，使用时需要根据场景继承定义，例如

```php
class SystemAuthVerify extends AuthVerify
{
    protected $scene = 'system';

    protected function hook(stdClass $symbol): bool
    {
        $data = AdminRedis::create()->get($symbol->user);
        if (empty($data)) {
            $this->hookResult = [
                'error' => 1,
                'msg' => 'freeze'
            ];
            return false;
        }
        return true;
    }
}
```

- **scene** `string` 场景标签
- **hook(stdClass $symbol): bool** 中间件钩子

然后在将中间件注册在应用的 `middleware.php` 配置下

```php
return [
    'auth' => \app\system\middleware\SystemAuthVerify::class
];
```

在控制器中重写 `$middleware`

```php
<?php

namespace app\system\controller;

class Index extends BaseController
{
    protected $middleware = ['auth'];

    public function index()
    {
        return [];
    }
}
```