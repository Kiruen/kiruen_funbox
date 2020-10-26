package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"net"
	"strings"
	"time"
)

func main() {
	listener, err := net.Listen("tcp", "localhost:8000")
	if err != nil {
		log.Fatal(err)
	}
	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Print(err) // e.g., connection aborted
			continue
		}
		go handleConn(conn) // handle one connection at a time
	}
}

func echo(c net.Conn, content string)  {
	ops := []func(string) string{strings.ToUpper, strings.Title, strings.ToLower }
	for i := 0; i < len(ops); i++{
		_, err := io.WriteString(c, fmt.Sprintf("%v\n", ops[i](content)))
		if err != nil {
			return
		}
		time.Sleep(500 * time.Millisecond)
	}
}

func handleConn(c net.Conn) {
	defer c.Close()
	input := bufio.NewScanner(c)
	for input.Scan() {
		content := input.Text()
		_, err := io.WriteString(c, time.Now().Format("15:04:05\n"))
		go echo(c, content)
		if err != nil {
			return // e.g., client disconnected
		}
		//time.Sleep(1 * time.Second)
	}
}