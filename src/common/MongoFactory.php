<?php

declare(strict_types=1);

namespace think\mgo\common;

use MongoDB\Client;
use MongoDB\Collection;
use MongoDB\Database;

/**
 * MongoDB 类
 * Class MongoFactory
 *
 * @package think\bit\common
 */
final class MongoFactory
{
    /**
     * 指向数据库
     * @var Database
     */
    private $database;

    /**
     * 构造处理
     * MongoFactory constructor.
     * @param array $config 配置信息
     */
    public function __construct(array $config)
    {
        $this->database = (new Client(
            $config['uri'],
            $config['uriOptions'],
            $config['driverOptions']
        ))->selectDatabase($config['database']);
    }

    /**
     * 指向集合
     * @param string $collectionName 集合名称
     * @param array $options 设置
     * @return Collection
     */
    public function name(string $collectionName, array $options = []): Collection
    {
        return $this->database->selectCollection(
            $collectionName,
            $options
        );
    }

    /**
     * 分页生成
     * @param string $collectionName 集合名称
     * @param array $filter 条件
     * @param int $page 页码
     * @param int $limit 分页数量
     * @param array $sort 排序条件
     * @return array
     */
    public function page(string $collectionName,
                         array $filter = [],
                         int $page = 1,
                         int $limit = 20,
                         array $sort = []): array
    {
        $total = $this->name($collectionName)
            ->countDocuments($filter);
        $lists = $this->name($collectionName)
            ->find(
                $filter,
                [
                    'skip' => $page - 1,
                    'limit' => $limit,
                    'sort' => $sort,
                ]
            )->toArray();

        return [
            'lists' => $lists,
            'total' => $total
        ];
    }
}
