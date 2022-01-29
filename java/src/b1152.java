import java.util.StringTokenizer;
import java.util.Scanner;

public class b1152 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.nextLine();
        in.close();
        StringTokenizer st = new StringTokenizer(S, " ");
        System.out.println(st.countTokens());
    }
}