//关键代码 不是全部逻辑 也不是只有c#才能调用 这是个例子
ProcessStartInfo startInfo = new ProcessStartInfo
        {
            FileName = PyExePath, // Python解释器的执行文件名
            Arguments = overwrite ? $"{pyPath} {imagePath} {cutType} {imagePath}" : $"{pyPath} {imagePath} {cutType}",
            RedirectStandardOutput = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        using Process process = new Process();
        process.StartInfo = startInfo;
        process.OutputDataReceived += (sender, e) =>
        {
            if (!string.IsNullOrEmpty(e.Data))
            {
                Debug.Log("输出数据：" + e.Data);
            }
        };

        process.Start();
        process.BeginOutputReadLine();
        process.WaitForExit();
