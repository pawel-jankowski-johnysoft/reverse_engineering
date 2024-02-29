import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws Exception {
        if (args.length < 1) {
            System.out.println("use: java Main.java <login>");
            System.exit(-1);
        }

        byte magic = (byte) ((0x539 * 0x20) / (0x10 * 0x10));


        byte[] input = args[0].getBytes();

        SecretKeySpec secretKeySpec = new SecretKeySpec( "13377331".getBytes(), "DES");
        Cipher cipher = Cipher.getInstance("DES");
        cipher.init(1, secretKeySpec);
        input = cipher.doFinal(input);

        secretKeySpec = new SecretKeySpec( "13248657".getBytes(), "DES");
        cipher.init(1, secretKeySpec);
        input = cipher.doFinal(input);

        System.out.print("password: ");
        for (byte b : input) {
            System.out.printf("%d ",  (b + magic));
        }

        System.out.println();
    }
}
