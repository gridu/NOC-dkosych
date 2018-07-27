import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Solution{
    private static String[] list;
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter objects in {a,b,c...} format");
        String s="";
        try {
            s = br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        int i,j;
        boolean fi=false,fj=false;
        for (i=0; i< s.length(); i++){
            if (s.charAt(i)==' ' || s.charAt(i)=='{')
                continue;
            else {
                fi=true;
                break;
            }
        }
        for (j=s.length()-1; j>=0; j--){
            if (s.charAt(j)==' ' || s.charAt(i)=='}')
                continue;
            else {
                fj=true;
                break;
            }
        }
        if (!fi || !fj || i>=j){
            System.out.print("Incorrect input");
            return;
        }
        String S1=s.substring(i,j);
        list=S1.split(",");
        for (int k=0; k<=list.length; k++){
            prin(k);
        }

    }
    private static void prin(int x){
        Integer[] ans=new Integer[x+1];
        for (int i=1; i<=x; i++)
            ans[i]=i;
        int k=x;
        if (k==0){
            System.out.print("{}, ");
        }
        while (k>=1){
            System.out.print("{");
            for(int i=1; i<ans.length; i++){
                System.out.print(list[ans[i]-1]);
                if (ans.length-i>1)
                    System.out.print(',');
            }
            System.out.print("}");
            if (x==list.length)
                break;
            System.out.print(", ");
            if (ans[x]==list.length)
                k--;
            else
                k=x;
            if (k>=1)
                for (int j=x; j>=k; j--)
                    ans[j]=ans[k]+j-k+1;
        }
    }
}
