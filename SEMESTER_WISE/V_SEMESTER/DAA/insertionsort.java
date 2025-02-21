public class insertionsort{
    public static void sort(int[] arr){
        for(int i=1; i<arr.length; i++){
            int key = arr[i];
            int j;
            for(j=i-1; j>=0 && arr[j]>key; j--){
                arr[j+1] = arr[j];
            }
            arr[j+1] = key;
        }
    }
        public static void main(String[] args){
            int[] arr = {12, 11, 13, 5, 6};
            sort(arr);
            for(int i=0; i<arr.length; i++){
                System.out.print(arr[i] + " ");
            }
        }
}