import java.util.Scanner;

class SubstringsOfAString
{
   public static void main(String args[])
   {
      String string, sub;
      int i, c, length;

      Scanner in = new Scanner(System.in);
      string  = in.nextLine();

      length = string.length();

      for( c = 0 ; c < length ; c++ )
      {
         for( i = 1 ; i <= length - c ; i++ )
         {
            sub = string.substring(c, c+i);
            System.out.println(sub);
         }
      }
   }
}
