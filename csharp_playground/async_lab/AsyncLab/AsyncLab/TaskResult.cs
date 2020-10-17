using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace AsyncLab
{
    public class TaskResult
    {
        public static Task<T> GetValueAsync<T>() where T: new()
        {
            return Task.FromResult(new T());
        }

        public static Task<T> GetTaskWithExceptionAsync<T>(string excMsg= "未知错误！！") where T : new()
        {
            var e = new TaskCompletionSource<T>();
            e.SetException(new Exception(excMsg));
            return e.Task;
        }
    }
}
