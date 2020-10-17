using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace AsyncLab
{
    public static class MyAwaitable
    {
        public static MyAwaiter GetMyAwaiter(this Task task)
        {
            return new MyAwaiter(task);
        }
    }

    public class MyAwaiter : INotifyCompletion
    {
        Task task;
        public MyAwaiter(Task task)
        {
            this.task = task;
        }

        public MyAwaiter GetAwaiter()
        {
            return this;
        }

        public bool IsCompleted
        {
            get =>  task.GetAwaiter().IsCompleted;
        }

        public void OnCompleted(Action continuation)
        {
            task.GetAwaiter().OnCompleted(continuation);
        }

        public void GetResult()
        {
            task.Wait();
        }
    }
}
