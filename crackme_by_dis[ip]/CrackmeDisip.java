public class CrackmeDisip {

    public static void main(String[] args) {
        if(args.length < 1) {
            System.out.println("run like: java <login> ");
            System.exit(1);
        }

        char magic = 'a';
        String login = args[0];
        StringBuilder password = new StringBuilder();
        for (char c : login.toCharArray()) {
            password.append((char) (c+1));
            password.append(magic);
            magic+=1;
        }
        password.trimToSize();
        System.out.println(password);
    }
}
