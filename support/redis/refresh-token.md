## Refresh Token 缓存

Refresh Token 是用于自动刷新、验证对应 Token 的缓存模型

### factory(string $jti, string $ack, int $expires): string

生产 Token 对应的 Refresh Token

- **jti** `string` JSON Web Token ID
- **ack** `string` Token ID 验证码
- **expires** `int` 存在时间，单位<秒>
- **Return** `string`

```php
$jti = Ext::uuid()->toString();
$ack = Str::random();

RefreshToken::create()->factory($jti, $ack, 86400*7);
```

### verify(string $jti, string $ack): bool

验证 Token 的 Token ID 有效性

- **jti** `string` JSON Web Token ID
- **ack** `string` Token ID 验证码
- **Return** `bool`

```php
RefreshToken::create()->verify($jti, $ack);
```

### clear(string $jti, string $ack): bool

清除 Token 对应的 Refresh Token

- **jti** `string` JSON Web Token ID
- **ack** `string` Token ID 验证码
- **Return** `bool`

```php
RefreshToken::create()->clear($jti, $ack);
```