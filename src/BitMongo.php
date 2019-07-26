<?php

namespace think\mgo;

use \MongoDB\Client;
use think\facade\Config;

/**
 * Class BitMongo
 * @package think\mgo
 */
final class BitMongo
{
    private $database;

    public function __construct()
    {
        $config = Config::get('database.mongodb');
        $client = new Client($config['uri'], $config['uriOptions'], $config['driverOptions']);
        $this->database = $client->selectDatabase($config['database']);
    }

    /**
     * 指向集合
     * @param string $collection 集合名称
     * @return \MongoDB\Collection
     */
    public function name($collection)
    {
        return $this->database->selectCollection($collection);
    }

    /**
     * 分页生成
     * @param string $collection 集合名称
     * @param array $filter 条件
     * @param int $page 页码
     * @param int $limit 分页数量
     * @param array $sort 排序条件
     * @return array
     */
    public function page($collection, $filter = [], $page = 1, $limit = 20, $sort = [])
    {
        $total = $this->name($collection)->countDocuments($filter);
        $lists = $this->name($collection)->find(
            $filter, [
            'skip' => $page - 1,
            'limit' => $limit,
            'sort' => $sort,
        ])->toArray();

        return [
            'lists' => $lists,
            'total' => $total
        ];
    }
}
