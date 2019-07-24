<?php

namespace think\mgo;

use MongoDB\Collection;
use think\Facade;

/**
 * Class Mgo
 * @package think\mgo
 * @method static Collection name($collection) 指向集合
 * @method static array page($collection, $filter = [], $page = 1, $limit = 20, $sort = []) 分页生成
 */
final class Mgo extends Facade
{
    protected static function getFacadeClass()
    {
        return BitMongo::class;
    }
}
