using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AdventofCode_2015_Task3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string path = @"prompt.txt";
            int x = 0;
            int y = 0;
            int rx = 0;
            int ry = 0;
            int turn = 0;
            string combination;

            List<string> uniqueLocations = new List<string>();

            string fs = File.ReadAllText(path);

            foreach (char direction in fs)
            {


                if (turn == 0) 
                {
                    if (direction == '^')
                    {
                        y++;
                    }
                    else if (direction == 'v')
                    {
                        y--;
                    }
                    else if (direction == '>')
                    {
                        x++;
                    }
                    else if(direction == '<')
                    {
                        x--;
                    }

                    combination = (x.ToString() + y.ToString());
                    turn++;
                }
                else
                {
                    if (direction == '^')
                    {
                        ry++;
                    }
                    else if (direction == 'v')
                    {
                        ry--;
                    }
                    else if (direction == '>')
                    {
                        rx++;
                    }
                    else if (direction == '<')
                    {
                        rx--;
                    }
                    combination = (rx.ToString() + ry.ToString());
                    turn--;
                }

                uniqueLocations.Add(combination);
                int distinctCount = uniqueLocations.Distinct().Count();

                Console.WriteLine(distinctCount);

            }
        }
    }
}
