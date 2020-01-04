package controller

import pb "redis-gRPC/router"

type controller struct {
	pb.UnimplementedRouterServer
}

func New() *controller {
	c := new(controller)
	return c
}
