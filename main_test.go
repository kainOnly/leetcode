package main

import (
	"github.com/go-redis/redis/v7"
	"github.com/sirupsen/logrus"
	"os"
	"testing"
	"time"
)

var client *redis.Client

func TestMain(m *testing.M) {
	client = redis.NewClient(&redis.Options{
		Addr:     "dell:6379",
		Password: "", // no password set
		DB:       2,  // use default DB
	})
	os.Exit(m.Run())
}

func TestSet(t *testing.T) {
	result, err := client.Set("test", "bv", time.Duration(time.Minute)).Result()
	if err != nil {
		t.Error(err)
	}
	logrus.Info(result)
}
