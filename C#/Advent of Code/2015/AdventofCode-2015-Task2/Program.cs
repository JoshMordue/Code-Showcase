using System;
using System.IO;

namespace AdventofCode_2015_Task2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string path = @"prompt.txt";
            int total = 0;
            int height;
            int width;
            int length;
            int size;
            int smallest;
            int volume;
            int ribbon;

            using (StreamReader sr = new StreamReader(path))
            {
                string line;
                var aribbon = 0;
                // Read and display lines from the file until the end of
                // the file is reached.
                while ((line = sr.ReadLine()) != null)
                {
                    //parsing the lines assigning to variables 
                    var results = line.Split('x');
                    length = int.Parse(results[0]);
                    width = int.Parse(results[1]);
                    height = int.Parse(results[2]);


                    //finding out answer to task 1
                    size = (2 * (length * width) + 2 * (width * height) + 2 * (height * length));

                    smallest = (System.Math.Min(System.Math.Min((length * width), (width * height)), (height * length)));

                    total += size + smallest;

                    //calculating the amount of ribbon for task 2
                    volume = (length * width * height);
                    ribbon = 2 * (System.Math.Min(System.Math.Min((length + width), (width + height)), (height + length)));

                    aribbon += volume + ribbon;

                    
                
                }
                Console.WriteLine(total);
                Console.Write(aribbon);


            }

        }
    }
}
