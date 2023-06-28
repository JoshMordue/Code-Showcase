using System;
using System.IO;
using System.Threading.Tasks;

namespace AdventofCode_2015_Task5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string path = @"prompt.txt";
            string line;
            int Task1 = 0;
            int Task2 = 0;

            using (StreamReader sentences = new StreamReader(path))
            {
                while ((line = sentences.ReadLine()) != null)
                {
                    Console.WriteLine($"The entered word: {line}");
                    if (CheckLine(line))
                    {
                        Task1++;
                        //Console.WriteLine("Succeeded");
                        //Console.WriteLine(counter);
                    }


                    if (CheckJump(line) && CheckDoubles(line))
                    {
                        Task2++;

                    }

                }

            }
            Console.WriteLine($"Task 1: {Task1}");
            Console.WriteLine($"Task 2: {Task2}");
        }


        static bool CheckLine(string line)
        {
            string[] illegalStrings = { "ab", "cd", "pq", "xy" };
            int vowelCount = 0;
            bool doubleLetter = false;

            //checking for illegal strings

            foreach (var nonoword in illegalStrings)
            {
                if (line.Contains(nonoword))
                {
                    //Console.WriteLine("This failed due to illegal string");
                    return false;
                }
            }


            for (int i = 0; i < line.Length; i++)
            {
                if (i > 0)
                {
                    if (line[i] == line[i - 1])
                    {
                        doubleLetter = true;
                    }
                }

                //checking for 3 vowels minimum
                if (line[i] == 'a' || line[i] == 'e' || line[i] == 'i' || line[i] == 'o' || line[i] == 'u')
                {
                    //Console.WriteLine(line[i]);
                    vowelCount++;
                }
            }

            if (vowelCount > 2 && doubleLetter == true)
            {
                return true;
            }
            else
            {
                //Console.WriteLine("Low Vowel count");
                return false;
            }
        }


        static bool CheckJump(string line)
        {
            bool jumpLetter = false;

            for (int i = 0; i < line.Length; i++)
            {

                if (i > 1)
                {
                    if (line[i] == line[i - 2])
                    {
                        jumpLetter = true;
                        //Console.WriteLine($"Found jump letters: {jumpLetter}");
                    }

                }

            }

            if (jumpLetter == true)
            {
                return true;
            }

            return false;
        }

        static bool CheckDoubles(string line)
        {
            bool matchFound = false;

            for (int i = 0; i < line.Length - 2; i++)
            {
                string thisPairOfTwoLetters = line[i] + line[i + 1].ToString();

                if (line.IndexOf(thisPairOfTwoLetters, i + 2, StringComparison.Ordinal) != -1)
                {
                    matchFound = true;
                    break;
                }
            }
            if (!matchFound)
                return false;
            return true;


        }
    }
}
        


    









