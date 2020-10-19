package main

import (
 "fmt"
 "io"
 "net/http"
 "os"
)

func main() {
 url_list := []string{"https://www.baidu.com", "https://www.qq.com", "http://gopl.io"}
 for _, url := range url_list {
  resp, err := http.Get(url)
  if err != nil {
   fmt.Println("错误！")
   os.Exit(1)
  }
  //data, err := ioutil.ReadAll(resp.Body)  //resp.Body是reader啊
  io.Copy(os.Stdout, resp.Body)
  //if err != nil {
  // fmt.Println("错误！")
  // os.Exit(1)
  //}
  //fmt.Println(string(data))
  resp.Body.Close()
 }
}
