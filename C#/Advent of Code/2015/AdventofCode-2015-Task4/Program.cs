using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;

namespace AdventofCode_2015_Task4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int counter = 1;
            string input = "ckczppom";
            string Hash;

            while (true)
            {
                Hash = CreateHash(input + counter);

                if (Hash.StartsWith("000000"))
                {

                    Console.WriteLine(counter);
                    break;
                }

                Console.WriteLine(Hash);

                counter++;
            }

        }

        public static string CreateHash(string input)
        {
            MD5 md5 = new MD5CryptoServiceProvider();

            //compute hash from the bytes of text  
            md5.ComputeHash(ASCIIEncoding.ASCII.GetBytes(input.ToString()));


            //get hash result after compute it  
            byte[] result = md5.Hash;

            StringBuilder strBuilder = new StringBuilder();
            for (int i = 0; i < result.Length; i++)
            {
                //change it into 2 hexadecimal digits  
                //for each byte  
                strBuilder.Append(result[i].ToString("x2"));
            }

            return strBuilder.ToString();

        }



    }
}
