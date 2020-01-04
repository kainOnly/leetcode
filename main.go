package main

import (
	"google.golang.org/grpc"
	"log"
	"net"
	"redis-gRPC/controller"
	pb "redis-gRPC/router"
)

func main() {
	listen, err := net.Listen("tcp", "127.0.0.1:6060")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	server := grpc.NewServer()
	pb.RegisterRouterServer(server, controller.New())
	server.Serve(listen)
}
