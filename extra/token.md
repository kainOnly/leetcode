## Token 令牌

Token 是 JSON Web Token 方案的功能服务，此服务必须安装 `kain/think-extra`，首先更新配置 `config/token.php`

```php
return [
    'system' => [
        'issuer' => 'system',
        'audience' => 'someone',
        'expires' => 3600,
    ],
];
```

当中 `system` `xsrf` 就是 `Token` 的 Label 标签，可以自行定义名称

- **issuer** `string` 发行者
- **audience** `string` 听众
- **expires** `int` 有效时间

安装后服务将自动注册可通过依赖注入使用

```php
use think\extra\contract\TokenInterface;

class Index extends BaseController
{
    public function index(TokenInterface $token)
    {
        $token->create('system', '12345678', 'a1b2');
    }
}
```

### create(string $scene, string $jti, string $ack, array $symbol = []): Plain

生成令牌

- **scene** `string` 场景标签
- **jti** `string` Token ID
- **ack** `string` Token 确认码
- **symbol** `array` 标识组
- **Return** `Lcobucci\JWT\Token\Plain`

```php
use think\support\facade\Token;

$token = Token::create('system', '12345678', 'a1b2');

dump($token->toString());

// "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkua2Fpbm9ubHkuY29tIiwiYXVkIjoiY29uc29sZS5rYWlub25seS5jb20iLCJqdGkiOiIxMjM0NTY3OCIsImFjayI6ImExYjIiLCJzeW1ib2wiOltdLCJleHAiOiIxNjA2MzY3MzQyLjUxMjA2MSJ9.YTIaJU2fBWIssxCu752DAM6yUlWOzJCTJFdsdkT18-0 ◀"
```

### get(string $jwt): Plain

获取令牌对象

- **jwt** `string` 字符串令牌
- **Return** `Lcobucci\JWT\Token\Plain`

```php
use think\support\facade\Token;

$jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkua2Fpbm9ubHkuY29tIiwiYXVkIjoiY29uc29sZS5rYWlub25seS5jb20iLCJqdGkiOiIxMjM0NTY3OCIsImFjayI6ImExYjIiLCJzeW1ib2wiOltdLCJleHAiOiIxNjA2MzY3MzQyLjUxMjA2MSJ9.YTIaJU2fBWIssxCu752DAM6yUlWOzJCTJFdsdkT18-0';

$token = Token::get($jwt);

dump($token);

// Lcobucci\JWT\Token\Plain {#78 ▼
//   -headers: Lcobucci\JWT\Token\DataSet {#87 ▼
//     -data: array:2 [▶]
//     -encoded: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
//   }
//   -claims: Lcobucci\JWT\Token\DataSet {#88 ▼
//     -data: array:6 [▶]
//     -encoded: "eyJpc3MiOiJhcGkua2Fpbm9ubHkuY29tIiwiYXVkIjoiY29uc29sZS5rYWlub25seS5jb20iLCJqdGkiOiIxMjM0NTY3OCIsImFjayI6ImExYjIiLCJzeW1ib2wiOltdLCJleHAiOiIxNjA2MzY3MzQyLjUxMjA2 ▶"
//   }
//   -signature: Lcobucci\JWT\Token\Signature {#90 ▼
//     -hash: b"a2\x1A%Mƒ\x05b,│\x10«´Øâ\x00╬▓RUÄ╠Éô$WlvD§¾Ý"
//     -encoded: "YTIaJU2fBWIssxCu752DAM6yUlWOzJCTJFdsdkT18-0"
//   }
// }
```

#### verify(string $scene, string $jwt): stdClass

验证令牌有效性

- **scene** `string` 场景标签
- **jwt** `string` 字符串令牌
- **Return** `stdClass`
  - **expired** `bool` 是否过期
  - **token** `Lcobucci\JWT\Token\Plain` 令牌对象

```php
use think\support\facade\Token;

$jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkua2Fpbm9ubHkuY29tIiwiYXVkIjoiY29uc29sZS5rYWlub25seS5jb20iLCJqdGkiOiIxMjM0NTY3OCIsImFjayI6ImExYjIiLCJzeW1ib2wiOltdLCJleHAiOiIxNjA2MzY3MzQyLjUxMjA2MSJ9.YTIaJU2fBWIssxCu752DAM6yUlWOzJCTJFdsdkT18-0';
$result = Token::verify('system', $jwt);

dump($result);
//{#94 ▼
//  +"expired": false
//  +"token": Lcobucci\JWT\Token\Plain {#89 ▼
//    -headers: Lcobucci\JWT\Token\DataSet {#90 ▼
//      -data: array:2 [▶]
//      -encoded: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
//    }
//    -claims: Lcobucci\JWT\Token\DataSet {#91 ▼
//      -data: array:6 [▶]
//      -encoded: "eyJpc3MiOiJhcGkua2Fpbm9ubHkuY29tIiwiYXVkIjoiY29uc29sZS5rYWlub25seS5jb20iLCJqdGkiOiIxMjM0NTY3OCIsImFjayI6ImExYjIiLCJzeW1ib2wiOltdLCJleHAiOiIxNjA2MzY3MzQyLjUxMjA2 ▶"
//    }
//    -signature: Lcobucci\JWT\Token\Signature {#93 ▼
//      -hash: b"a2\x1A%Mƒ\x05b,│\x10«´Øâ\x00╬▓RUÄ╠Éô$WlvD§¾Ý"
//      -encoded: "YTIaJU2fBWIssxCu752DAM6yUlWOzJCTJFdsdkT18-0"
//    }
//  }
//}
```