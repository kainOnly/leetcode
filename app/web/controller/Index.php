<?php

namespace app\http\web\controller;

use app\BaseController;

class Index extends BaseController
{
    public function index()
    {
        return json([
            'error' => 1
        ]);
    }

    public function xxx()
    {
        return json([
            'name' => 'kain'
        ]);
    }
}
