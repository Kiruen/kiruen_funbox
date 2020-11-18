package main

func main() {
	//bc := NewBlockchain()
	//defer bc.db.Close()
	//os.Args = append(os.Args, "createblockchain")
	//fmt.Println(os.Args)
	cli := CLI{}
	cli.Run()
}
