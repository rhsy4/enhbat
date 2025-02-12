public class main {
    import java.util.Scanner;

public class Hicheell {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Улирлын дугаарыг оруулна уу (1-Хавар, 2-Зун, 3-Намар, 4-Өвөл): ");
        int season = scanner.nextInt();
        
        switch (season) {
            case 1:
                printSpring();
                break;
            case 2:
                printSummer();
                break;
            case 3:
                printFall();
                break;
            case 4:
                printWinter();
                break;
            default:
                System.out.println("Буруу утга оруулсан байна. 1-4 хоорондын тоо оруулна уу.");
        }
        
        scanner.close();
    }
    
    public static void printSpring() {
        System.out.println("Хавар болж цэцэгс цэцэглэлээ.");
    }
    
    public static void printSummer() {
        System.out.println("Зун болж халуун боллоо.");
    }
    
    public static void printFall() {
        System.out.println("Намар болж навч уналаа.");
    }
    
    public static void printWinter() {
        System.out.println("Өвөл болж цас орлоо.");
    }
}

}
