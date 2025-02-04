import java.util.*;
public class helloworld3 
{
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int saving = sc.nextInt();
    sc.nextLine();
    int n = sc.nextInt();
    sc.nextLine();
    int[] currentvalue = new int[n];
    for(int i=0; i<n; i++){
        currentvalue[i] = sc.nextInt();
    }
    sc.nextLine();
    int a = sc.nextInt();
    sc.nextLine();
    int[] futurevalue = new int[a];
    for(int i=0; i<a; i++){
        futurevalue[i] = sc.nextInt();
    }
    int[] dp = new int[saving + 1];
    for(int i=0; i<n; i++){
        for(int j=saving;j>=currentvalue[i];j--)
        {
            dp[j] = Math.max(dp[j],dp[j-currentvalue[i]]+futurevalue[i]-currentvalue[i]);

        
        }   
}
System.out.println(dp[saving]);
    
}
}