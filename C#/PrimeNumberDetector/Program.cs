using System;


namespace PrimeNumberDetector
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int userNumber;
            while (true)
            {
                Console.WriteLine("Please enter a number you want to check whether it is prime: ");
                userNumber = Convert.ToInt32(Console.ReadLine());

                if (checkNumber(userNumber))
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"{userNumber} is a prime number.");
                    Console.ResetColor();

                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"{userNumber} is not a prime number.");
                    Console.ResetColor();
                }

                Console.WriteLine();
            }

            bool checkNumber(int Number)
                //the function uses the number provided to ascertain whether the number is a prime number or not.
            {
                if (Number <= 1) return false;
                if (Number == 2) return true;
                if (Number % 2 == 0) return false;

                int boundary = (int)Math.Floor(Math.Sqrt(Number));

                for (int i = 3; i <= boundary; i += 2)
                    if (Number % i == 0)
                        return false;

                return true;
            }
            


        }

    }


}

