using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace Palindrome
{
    class PalindromeChecker
    {

        private static int textIter;
        private static int lastChar;

        static void Main(string[] args)
        {
            //the user will be presented with a brief welcome message and will be prompted to enter a word to check for a palindrome.
            //the word will be checked to ensure there are no numbers, the word is longer than 3 letters and there's no empty field.
            //once the criteria has been met their input (inputText variable) will be sent to the InputCheck for comparison.
            string inputText;

            Console.WriteLine(String.Format("{0," + Console.WindowWidth / 2 + "}", "Palindrome Checker"));
            Console.WriteLine(String.Format("{0," + Console.WindowWidth / 2 + "}", "**********************************************************************"));
            Console.WriteLine(String.Format("{0," + Console.WindowWidth / 2 + "}", "Please enter a word/Sentence and we see if it is a palindrome."));
            Console.WriteLine(String.Format("{0," + Console.WindowWidth / 2 + "}", "Please note when comparing a sentence spaces will not be considered."));
            Console.WriteLine(String.Format("{0," + Console.WindowWidth / 2 + "}", "**********************************************************************"));
            while (true) {

                inputText = Console.ReadLine();
                bool isAlpha = Regex.IsMatch(inputText, @"^[a-zA-Z ]+$");

                if (!String.IsNullOrEmpty(inputText) && inputText.Length > 3)
                {
                    Console.WriteLine($"{inputText} was entered.");
                    InputCheck(inputText);
                }
                else
                {
                    Console.WriteLine($"{inputText} was not valid, Please ensure the word entered is not using numbers");
                }

            }
        }

        public static string InputCheck(string Text) 
        {
            //The function receives the inputted string, then the "textIter" variable will get the letter count of the string divided by 2.
            // As we're checking for a palindrome we do not require half the other characters being tested since it already has been.
            // the "lastChar" variable is to compare the first letter with the last. if all the letters match by the middle (textIter)
            // number it'll return the word being a palindrome.

            textIter = (lastChar / 2);
            lastChar = Text.Count() - 1;


            for (int i = 0; i < textIter; i += 1)
            {
                if (Text[i] < Text[lastChar])
                {
                    Console.WriteLine($"{Text} is not palindrome.");
                    return Text;
                }

                lastChar -= 1;

            }

            Console.WriteLine($"{Text} is a palindrome.");
            return Text;
        }
    }
}
