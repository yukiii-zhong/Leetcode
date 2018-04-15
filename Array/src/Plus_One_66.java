import java.util.Arrays;
import java.util.stream.Stream;

public class Plus_One_66 {
    public int[] plusOne(int[] digits){
        for (int i = digits.length-1; i>=0; i--){
            digits[i]++;
            if (digits[i] <10){
                return digits;
            }
            else{
                digits[i] = 0;
            }
        }
        if (digits[0] == 0){
           int[] newDigits=new int[digits.length+1];
           newDigits[0] =1;
           for (int i=0;i<digits.length;i++){
               newDigits[i+1] = digits[i];
           }
           digits = newDigits;
        }
        return digits;
    }
}
