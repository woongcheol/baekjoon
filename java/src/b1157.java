import java.util.Scanner;

public class b1157 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[] arr = new int[26];
        String s = in.next();

        for (int i = 0; i < s.length(); i++){

            if (65 <= s.charAt(i) && s.charAt(i) <= 90) {
                arr[s.charAt(i) - 65]++;
            }

            else {
                arr[s.charAt(i) - 97]++;
            }
        }

        int max = -1;
        char ch = '?';

        for (int i = 0; i < 26; i++) {
            if (arr[i] > max) {
                max = arr[i];
                ch = (char) (i + 65);
            }
            else if (arr[i] == max) {
                ch = '?';
            }
        }

        System.out.println(ch);
        System.out.println(arr);
    }

}