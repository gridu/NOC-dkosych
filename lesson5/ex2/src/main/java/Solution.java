import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Solution {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter N array of K element in {a,b} ,{c,..},..} format");
        String s = "";
        try {
            s = br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        Set<String> ar = new TreeSet<>();
        int y = 0;
        List<Integer> str = new ArrayList<Integer>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '{') {
                if (y % 2 == 0) {
                    str.add(i);
                    y++;
                } else {
                    System.out.print("Incorrect input");
                    return;
                }
            }
            if (s.charAt(i) == '}') {
                if (y % 2 == 1) {
                    str.add(i);
                    y++;
                } else {
                    System.out.print("Incorrect input");
                    return;
                }
            }
        }
        String sub;
        for (int i = 0; i < str.size(); i += 2) {
            sub = s.substring(str.get(i) + 1, str.get(i + 1));
            String[] subSpl = sub.split(",");
            for (int j = 0; j < subSpl.length; j++) {
                if (!ar.contains(subSpl[j])) {
                    ar.add(subSpl[j]);
                }
            }
        }
        int n = ar.size() * ar.size();
        System.out.println("Number of pairs = " + n);
        for (String x : ar) {
            for (String z : ar) {
                if (n > 1) {
                    System.out.print("(" + x + ", " + z + "), ");
                    n--;
                } else {
                    System.out.print("(" + x + ", " + z + ")");
                }

            }
        }

    }
}
