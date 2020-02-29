package controller

import (
	"context"
	pb "redis-microservice/router"
)

func (c *controller) Get(ctx context.Context, query *pb.GetParameter) (*pb.GetResponse, error) {
	return &pb.GetResponse{
		Value: "test:" + query.Key,
	}, nil
}

func (c *controller) Set(ctx context.Context, query *pb.SetParameter) (*pb.SetResponse, error) {
	return &pb.SetResponse{
		Result: true,
	}, nil
}
