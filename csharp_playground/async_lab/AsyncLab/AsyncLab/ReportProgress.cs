using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace AsyncLab
{
    public class ReportProgress
    {
        public static bool done;
        public async static Task<int> CreateTaskWithProgress(IProgress<int> progresser)
        {
            int val = 0;
            while(!done)
            {
                progresser?.Report(val++);
                await Task.Delay(1000);
            }
            //return TaskResult.GetValueAsync<int>();
            return val; //await Task.FromResult(val)
        }

        public async static Task<string> ExecOneTask()
        {
            var progresser = new Progress<int>();
            progresser.ProgressChanged += Progresser_ProgressChanged;
            var res = await CreateTaskWithProgress(progresser);
            return $"最终结果：{res}";
        }

        private static void Progresser_ProgressChanged(object sender, int e)
        {
            Console.WriteLine(e);
            if(e == 10)
            {
                done = true;
            }
        }
    }
}
