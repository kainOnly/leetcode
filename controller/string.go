package controller

import (
	"context"
	pb "gRPC-redis/router"
)

func (c *controller) Get(ctx context.Context, query *pb.GetParameter) (*pb.GetResult, error) {
	return &pb.GetResult{
		Value: "test:" + query.Key,
	}, nil
}

func (c *controller) Set(ctx context.Context, query *pb.SetParameter) (*pb.SetResult, error) {
	return &pb.SetResult{
		Result: true,
	}, nil
}
