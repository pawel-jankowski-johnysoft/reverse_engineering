import java.util.Random;
import static java.util.Arrays.stream;
class Main {
    private static final int JMP_OPCODE_OFFSET_TO_UPDATE = 62;
    private static final int CODE_OFFSET_TO_UPDATE = 0x1c;
    public static void main(String[] args) {

        if(args.length < 1) {
            System.err.println("use: java Main <login>");
            System.exit(1);
        }

        int charsSumPowered = (int) Math.pow(args[0].chars().sum(), 2);
        int expectedHashedPasswordLastByte = (charsSumPowered ^ CODE_OFFSET_TO_UPDATE) & 0xff;
        System.out.println(String.join("-", String.valueOf(JMP_OPCODE_OFFSET_TO_UPDATE), generatePassword(expectedHashedPasswordLastByte)));
    }

    private static String generatePassword(int requiredLastByteValue) {
        Random random = new Random();
        while (true) {
            int[] potentialPasswordCharacters = random.ints(random.nextInt(6,12), 'a', 'z').toArray();
            if((-stream(potentialPasswordCharacters).sum() & 0xff) == requiredLastByteValue) {
                StringBuilder password = new StringBuilder();
                stream(potentialPasswordCharacters).forEach(password::appendCodePoint);
                password.trimToSize();
                return password.toString();
            }
        }
    }
}


