using System;
using System.IO;

namespace AdventofCode_2015_Task1
{
    internal class Program
    {

        static void Main(string[] args)
        {
            int floor = 0;
            int descent_count = 1;
            bool countFound = false;
            string path = @"prompt.txt";

            string fs = File.ReadAllText(path);

            //( means up a floor
            //) means down a floor

            foreach (char line in fs)
            {
                if (line == ')')
                {
                    floor--;
                    descent_count++;
                    if (floor == -1 && countFound == false)
                    {
                        Console.WriteLine($"The character position where it passed into the basement is: {descent_count}");
                        countFound = true;
                    }
                }
                else
                {
                    floor++;
                    descent_count++;
                }
            }
            Console.WriteLine($"The final floor is {floor}");
            
                  

        }
    }
}
