<?php

namespace think\mgo\facade;

use MongoDB\Collection;
use think\Facade;

/**
 * Class Mongo
 * @method static Collection name(string $collectionName, array $options = [])
 * @method static array page(string $collectionName, array $filter = [], int $page = 1, int $limit = 20, array $sort = [])
 * @package think\mgo\facade
 */
class Mongo extends Facade
{
    protected static function getFacadeClass(): string
    {
        return 'mongo';
    }
}