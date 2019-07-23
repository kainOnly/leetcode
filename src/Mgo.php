<?php

namespace think\mgo;

use MongoDB\Database;
use think\Facade;

/**
 * Class Mgo
 * @package think\mgo
 * @method static Database Db($database = '') 指向数据库
 * @method static array Page($database, $collection, $filter = [], $page = 1, $limit = 20, $sort = ['create_time' => -1]) 分页生成
 */
final class Mgo extends Facade
{
    protected static function getFacadeClass()
    {
        return BitMongo::class;
    }
}
