package instances

import (
	"errors"
	"github.com/go-redis/redis/v7"
	"time"
)

type Instances struct {
	client  map[string]*redis.Client
	options map[string]*redis.Options
}

func NewInstances() *Instances {
	instances := new(Instances)
	instances.client = make(map[string]*redis.Client)
	instances.options = make(map[string]*redis.Options)
	return instances
}

func (c *Instances) empty(identity string) error {
	if c.client[identity] == nil || c.options[identity] == nil {
		return errors.New("this identity does not exists")
	}
	return nil
}

func (c *Instances) Close(identity string) error {
	if err := c.empty(identity); err != nil {
		return err
	}
	return c.client[identity].Close()
}

func (c *Instances) Ping(identity string) (string, error) {
	if err := c.empty(identity); err != nil {
		return "", err
	}
	return c.client[identity].Ping().Result()
}

func (c *Instances) Set(identity string, key string, val interface{}, exp time.Duration) (string, error) {
	if err := c.empty(identity); err != nil {
		return "", err
	}
	return c.client[identity].Set(key, val, exp).Result()
}

func (c *Instances) Get(identity string, key string) (string, error) {
	if err := c.empty(identity); err != nil {
		return "", err
	}
	return c.client[identity].Get(key).Result()
}
