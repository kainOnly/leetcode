package client

import (
	"context"
	"google.golang.org/grpc"
	"log"
	"os"
	pb "redis-microservice/router"
	"testing"
)

var (
	conn   *grpc.ClientConn
	client pb.RouterClient
	err    error
)

func TestMain(m *testing.M) {
	conn, err = grpc.Dial("127.0.0.1:1000", grpc.WithInsecure())
	if err != nil {
		log.Fatalln(err)
	}
	client = pb.NewRouterClient(conn)
	os.Exit(m.Run())
}

func TestSet(t *testing.T) {
	var response *pb.GetResponse
	defer conn.Close()
	response, err = client.Get(context.Background(), &pb.GetParameter{
		Key: "kain",
	})
	if response.Value != "test:kain" {
		t.Error("neq")
	}
}
