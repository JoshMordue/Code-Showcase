using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace AdventofCode_2015_Task6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string path = @"prompt.txt";
            string line;
            int startRange1;
            int endRange1;
            int startRange2;
            int endRange2;
            string command;



            using (StreamReader sentences = new StreamReader(path))
            {
                while ((line = sentences.ReadLine()) != null)
                {
                    if (line.StartsWith("turn off"))
                    {
                        command = "turn off";
                        line = StripLine(command, line);
                        FindRanges(line, startRange1, endRange1, startRange2, endRange2);
                    }
                    else if (line.StartsWith("turn on"))
                    {
                        command = "turn on";
                        line = StripLine(command, line);
                         FindRanges(line, startRange1, endRange1, startRange2, endRange2);
                    }
                    else if (line.StartsWith("toggle"))
                    {
                        command = "toggle";
                        line = StripLine(command, line);
                        FindRanges(line, startRange1, endRange1, startRange2, endRange2);
                    }
                    else
                    {
                        Console.Write("RUN BAD INPUT");
                    }
                }
            }

        }

        static string StripLine(string command, string line)
        {
            line = line.Replace(command, "").Replace("through", ",");
            return line;
        }

        static string FindRanges(string line, int startRange1, int endRange1, int startRange2, int endRange2)
        {

           startRange1, endRange1, startRange2, endRange2 = line.Split(','); 

        }



    }
}

