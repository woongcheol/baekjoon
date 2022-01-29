import java.util.Scanner;

public class b1008 {
    // https://seeminglyjs.tistory.com/149 참고
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        double answer = a*1.0/b;
        System.out.println(answer);
        in.close();
    }
}