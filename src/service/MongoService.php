<?php

declare (strict_types=1);

namespace think\redis\service;

use think\Service;
use think\mgo\common\MongoFactory;

final class MongoService extends Service
{
    public function register(): void
    {
        $this->app->bind('mongo', function () {
            $config = $this->app->config
                ->get('database.mongodb');

            return new MongoFactory($config);
        });
    }
}