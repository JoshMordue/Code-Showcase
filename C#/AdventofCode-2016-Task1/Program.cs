using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace AdventofCode_2016_Task1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string path = @"prompt.txt";
            string line = "";

            using (StreamReader sentences = new StreamReader(path))
            {
                while ((line = sentences.ReadLine()) != null)
                {




                }
            }
        }
    }
}
