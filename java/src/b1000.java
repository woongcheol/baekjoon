import java.util.Scanner;
// Scanner 메소드를 사용하기 위해 java.util 패키지를 import 한다.

public class b1000 {

    public static void main(String[] args) {
        // Scanner new Scanner(System.in);
        //        int a = sc.nextInt();메소드 사용
        // 1. 대부분 공백과 개행(' ', '\t', '\r', '\n' 등등..)을 기준으로 읽음
        // 2. 입럭을 위해 Scanner 클래스 호출 및 생성
        // 3. 객체 이름은 보통 in, input, sc, scan 으로 작성
        // 4. System.in은 사용자로부터 입력을 받기 위한 입력 스트림
        Scanner sc =
        int b = sc.nextInt();

        System.out.println(a+b);

        sc.close();

    }
}