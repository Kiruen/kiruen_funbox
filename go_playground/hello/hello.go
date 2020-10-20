package main
//go语言的入门程序

import (
 "bufio"
 "fmt"
 "io/ioutil"
 "os"
 "strings"
)

func main0() {
 a := 1
 var s1, s2 string
 s1, s2 = "_s1_", "_s2_"
 for a < 10 {
  fmt.Print(a, s1, s2)
  a++
 }
 for b := 1; b < 10; b++ {
  fmt.Print(a + b, "  ")
 }
 fmt.Println("asdasd")
 fmt.Println(1 + 2 / 5)
 fmt.Println(os.Args[0:])
 fmt.Println(a)
 //l := [1,2,3]

 var c, _ int = 1, 2
 var d, e string = "ddd", "eee"
 var f, g = "ffff", 1111
 var h float32
 fmt.Println(c, d, e, f, g, h)
 //fmt.Println(strings.Join(, " "))

 for i, v := range os.Args {
  fmt.Println(i, v)
 }


 files := os.Args[1:]
 if len(files) == 0 {
  counts := make(map[string]int)
  input := bufio.NewScanner(os.Stdin)
  for input.Scan() {
   counts[input.Text()] ++
  }
  for line, n := range counts {
   if n > 0 {
    fmt.Printf("%s 's count is %d\n", line, n)
   }
  }
 } else {
  for _, fileName := range files {
    f, err := os.Open(fileName)
    text, _ := ioutil.ReadFile(fileName)
    if err != nil {
     fmt.Fprintf(os.Stderr, "dup2: %v", err)
     continue
    }
    fmt.Printf("文件的lines: %v\n", strings.Split(string(text), "\r\n"))
    counts := countLines(f)
    fmt.Println(counts)
  }
 }
}

func countLines(f *os.File) map[string]int {
 counts := make(map[string]int)
 input := bufio.NewScanner(f)
 for input.Scan() {
  counts[input.Text()] ++
 }
 return counts
}