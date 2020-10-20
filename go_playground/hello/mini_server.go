package main

import (
 "fmt"
 "log"
 "net/http"
 "strings"
)

type Counter struct {
 testCount, gifCount int
}
var counter Counter

func main() {
 http.HandleFunc("/test", handler)
  http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
  switch {
  case strings.Contains(r.URL.Path, "a"):
   fmt.Fprintf(w, "你有a")
  default:
   fmt.Fprintf(w, "你没有a")
  }
 })
 http.HandleFunc("/gif", handler_gif)
 log.Fatal(http.ListenAndServe("localhost:8000", nil))
}


func handler(w http.ResponseWriter, r *http.Request) {
//r.PostForm
 fmt.Fprintf(w,"request: %v\n\n\n", r)
 fmt.Fprintf(w,"host: %s\n", r.Host)
 fmt.Fprintf(w,"%s %s %s\n", r.Method, r.Proto, r.URL)
 for k, v := range r.Header {
  fmt.Fprintf(w, "header[%q] = %q\n", k, v)
 }
 for k, v := range r.Form {
   fmt.Fprintf(w, "form[%q] = %q\n", k, v)
 }
 if err := r.ParseForm(); err != nil {
  return
 }
 counter.testCount ++
 fmt.Fprintf(w, "Counter: %v", counter)
}

func handler_gif(w http.ResponseWriter, r *http.Request) {
 lissajous(w)
 counter.gifCount ++
}

