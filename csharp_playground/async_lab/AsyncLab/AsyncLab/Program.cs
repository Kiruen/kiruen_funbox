using System;
using System.Collections.Generic;
using System.IO;
using System.Threading;
using System.Threading.Tasks;

namespace AsyncLab
{
    class Program
    {
        async static Task PossibleExceptionAsync()
        {
            await Task.Delay(5000);
            File.ReadAllText("test.txt");
        }

        async static Task<int> DoSomethingAndWait(int n)
        {
            await Task.Delay(TimeSpan.FromMilliseconds(n)).ConfigureAwait(false);
            //Thread.Sleep(n);
            //Console.WriteLine(n);
            //Thread.Sleep(1);
            Console.WriteLine($"TID: {Thread.CurrentThread.ManagedThreadId}");
            await Task.Delay(n);
            //Console.WriteLine(Math.Pow(n, 3));
            return n;
        }

        async static Task DoSomethingWithExcpt()
        {
            var task = PossibleExceptionAsync();  //居然不用await，就已经开始跑了，
            try
            {
                await task;  
                //如果同步(无async)执行，会怎么样？await统统不执行了？
                //不是，没async的话不会异步调用了，将会严格顺序执行。等待delay也失效
            }
            catch (Exception e)
            {
                //throw;
                Console.WriteLine(e);
            }
        }

        static async Task Main(string[] args)
        {
            Console.WriteLine($"TID: {Thread.CurrentThread.ManagedThreadId}");
            var tasks = new List<Task<int>>();
            for (int i = 200; i < 1000; i+=100)
            {
                //Task.Run<int>(DoSomethingAndWait);
                tasks.Add(DoSomethingAndWait(i));  //已经开始跑了
            }
            foreach (var task in tasks)
            {
                Console.Write($"{task.Result}, ");
            }
            
            await DoSomethingWithExcpt();

            Console.WriteLine("OK");
            Console.ReadLine();
        }
    }
}
