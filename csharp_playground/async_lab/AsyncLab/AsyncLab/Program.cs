using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;

namespace AsyncLab
{
    class Program
    {
        async static Task<string> DownloadWithTimeout(string url, int timeout=1000)
        {
            using (var client = new HttpClient())
            {
                var t_download = client.GetStringAsync(url);
                var t_timeout = Task.Delay(timeout);
                var t_compeleted = await Task.WhenAny(t_timeout, t_download);
                if (t_compeleted == t_timeout)
                {
                    return "Timeout!";
                }
                return await t_download; //await t_compeleted;
            }

        }

        async static Task PossibleExceptionAsync()
        {
            await Task.Delay(5000);
            File.ReadAllText("test.txt");
        }

        async static Task<T> DoSomethingAndWait<T>(int n, T res)
        {
            await Task.Delay(TimeSpan.FromMilliseconds(n)).ConfigureAwait(false);
            //Thread.Sleep(n);
            //Console.WriteLine(n);
            //Thread.Sleep(1);
            Console.WriteLine($"TID: {Thread.CurrentThread.ManagedThreadId}");
            await Task.Delay(n);
            //Console.WriteLine(Math.Pow(n, 3));
            return res;
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

        static async Task Foo1(string[] args)
        {
            Console.WriteLine($"TID: {Thread.CurrentThread.ManagedThreadId}");
            var tasks = new List<Task<double>>();
            for (int i = 200; i < 1000; i += 100)
            {
                //Task.Run<int>(DoSomethingAndWait);
                tasks.Add(DoSomethingAndWait(i, Math.Pow(i, 2)));  //已经开始跑了
            }
            foreach (var task in tasks)
            {
                //Console.Write($"{task.Result}, ");  //一样的
                Console.Write($"{await task}, ");
            }

            //await DoSomethingWithExcpt();
            Console.WriteLine(await DownloadWithTimeout("https://www.google.com"));
            Console.WriteLine(await TaskResult.GetValueAsync<decimal>());

            /*
            //Console.WriteLine(await TaskResult.GetTaskWithExceptionAsync<double>());  //await处截获异常并抛出
            var taske = Task.WhenAll(TaskResult.GetTaskWithExceptionAsync<double>(),
                TaskResult.GetTaskWithExceptionAsync<int>("哈哈哈，出错了吧！"));
            await taske.GetMyAwaiter(); //taske.GetMyAwaiter().GetResult();
            //await taske; //Result awaiter.GetReult 都一样，但task.wait会抛出aggregate
            */

            //Console.WriteLine(ReportProgress.ExecOneTask()); 这个
            Console.WriteLine(await ReportProgress.ExecOneTask());
        }

        static async Task Main(string[] args)
        {


            Console.WriteLine("OK");
            Console.ReadLine();
        }
    }
}
