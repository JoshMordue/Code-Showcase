using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class cardHolder
{
    string cardNum;
    int pin;
    string firstName;
    string lastName;
    decimal balance;

    public cardHolder(string cardNum, int pin, string firstName, string lastName, decimal balance)
    {
        this.cardNum = cardNum;
        this.pin = pin;
        this.firstName = firstName;
        this.lastName = lastName;
        this.balance = balance;
    }

    public int GetPin()
    {
        return pin;
    }

    public string GetFirstName()
    {
        return firstName;
    }

    public string GetLastName()
    {
        return lastName;
    }

    public decimal GetBalance()
    {
        return balance;
    }



    public void SetBalance(decimal newBalance)
    {
        balance = newBalance;
    }

    public static void Main(String[] args)
    {
        void printOptions()
        {
            //Prints the menu containing their options
            Console.WriteLine("Please choose from the following options:");
            Console.WriteLine("1: Show Balance");
            Console.WriteLine("2: Deposit");
            Console.WriteLine("3: Withdraw");
            Console.WriteLine("4: Exit");
        }

        void Deposit(cardHolder CurrentUser)
        {
            //Prompts the user the amount of currency the user would like added to their account then adds it to their total balance.
            Console.WriteLine("Depositing");
            Console.WriteLine("**************");
            Console.WriteLine("How much would you like to deposit? ");
            decimal deposit = Decimal.Parse(Console.ReadLine());
            CurrentUser.SetBalance(deposit + CurrentUser.GetBalance());
        }

        void Withdraw(cardHolder CurrentUser)
        {
            //Prompts the user the amount of currency the user would like withdrawn from their account,
            //Checks to ensure they have enough money then subtracts the amount from their total balance.
            Console.WriteLine("Withdrawing");
            Console.WriteLine("**************");
            Console.WriteLine("How much would you like to withdraw? ");
            decimal withdraw = Decimal.Parse(Console.ReadLine());
            if (CurrentUser.GetBalance() < withdraw)
            {
                Console.WriteLine("Insufficient Balance");
            }
            else
            {
                CurrentUser.SetBalance(CurrentUser.GetBalance() - withdraw);
                Console.WriteLine($"You've successfully withdrawn: {withdraw}, New Balance is: {CurrentUser.GetBalance()}");
            }
        }

        void Balance(cardHolder CurrentUser)
        {
            //Provides the user information on their total account balance.
            Console.WriteLine("Current Balance: " + CurrentUser.GetBalance());
        }

        List<cardHolder> cardHolders = new List<cardHolder>();
        cardHolders.Add(new cardHolder("4003830171874018", 5456, "Anne", "Jessop", 1000));
        cardHolders.Add(new cardHolder("8936474640510142", 7216, "Terry", "Banks", 62.34m));
        cardHolders.Add(new cardHolder("6013585142342681", 4563, "Sean", "Deacon", 5478.87m));
        cardHolders.Add(new cardHolder("0730898193825365", 2488, "Ben", "King", 780.55m));

        //Prompts the user to enter their debit card number.
        Console.WriteLine("Welcome to the SimpleATM");
        Console.WriteLine("Please enter your debit card number:");

        string debitCardNum;
        int userPin;
        cardHolder currentUser;

        while (true)
        {
            try
            {
                debitCardNum = Console.ReadLine();
                //check against the database for a matching debit card number
                currentUser = cardHolders.FirstOrDefault(a => a.cardNum == debitCardNum);
                if (currentUser != null)
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Card is not recognised. Please try again.");
                }
            }
            catch
            {
                Console.WriteLine("Card is not recognised. Please try again.");

            }
        }

        Console.WriteLine("Please enter your pin: ");
        while (true)
        {
            try
            {
                //prompts the user to enter the matching pin number associated with their card number.
                userPin = int.Parse(Console.ReadLine());
                if (currentUser.GetPin() == userPin)
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Incorrect Pin, Please try again");
                }
            }
            catch
            {
                Console.WriteLine("Incorrect Pin, Please try again");

            }

        }

        Console.WriteLine("Welcome " + currentUser.GetFirstName() + " " + currentUser.GetLastName());
        int option = 0;

        do
        {
            printOptions();
            try
            {
                option = int.Parse(Console.ReadLine());
                switch (option)
                {
                    case 1:
                        Balance(currentUser);
                        break;
                    case 2:
                        Deposit(currentUser);
                        break;
                    case 3:
                        Withdraw(currentUser);
                        break;                    
                }
            }
            catch
            {
                Console.WriteLine("Error selecting an option, please reload the application.");
            }
        }
        while (option != 4);
        {
            Console.WriteLine("Thank you for using the SimpleATM, Have a great day!");
        }

    }

}


