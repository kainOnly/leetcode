<?php

namespace app\system\controller;

use app\BaseController;
use app\system\repository\AccessTokenRepository;
use app\system\repository\ClientRepository;
use app\system\repository\ScopeRepository;
use League\OAuth2\Server\AuthorizationServer;
use think\facade\Config;

class Index extends BaseController
{
    public function index()
    {
        $server = new AuthorizationServer(
            new ClientRepository(),
            new AccessTokenRepository(),
            new ScopeRepository(),
            Config::get('oauth.private'),
            Config::get('oauth.encryptionKey')
        );

        dump($server);
//        return json([
//            'error' => 0
//        ]);
    }

    public function access_token()
    {
        return 'ok';
    }
}
