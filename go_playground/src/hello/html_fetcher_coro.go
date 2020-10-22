package main

import (
 "fmt"
 "io"
 "io/ioutil"
 "net/http"
 "strings"
 "time"
)

func main3() {
 url_list := []string{"https://www.baidu.com", "https://www.qq.com"} //, "http://gopl.io"
 fmt.Println(strings.Join(url_list, ", "))
 start := time.Now()
 ch := make(chan string)
 for _, url := range url_list {
  go fetch(url, ch)
 }
 for range url_list {
  fmt.Println(<-ch)
 }
 fmt.Printf("time spanned: %v", time.Since(start).Seconds())
}

func fetch(url string, ch chan<- string) {
 start := time.Now()
 resp, _ := http.Get(url)
 nbytes, _ := io.Copy(ioutil.Discard, resp.Body)
 resp.Body.Close()
 secs := time.Since(start).Seconds()
 ch <- fmt.Sprintf("%.2fs  %7d  %s", secs, nbytes, url)
}