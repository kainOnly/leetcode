package main

import (
	"gRPC-redis/controller"
	pb "gRPC-redis/router"
	"google.golang.org/grpc"
	"log"
	"net"
)

func main() {
	listen, err := net.Listen("tcp", "127.0.0.1:1000")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	server := grpc.NewServer()
	pb.RegisterRouterServer(server, controller.New())
	server.Serve(listen)
}
