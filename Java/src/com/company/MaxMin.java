package com.company;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class MaxMin {
    // Complete the maxMin function below.
    static int maxMin(int k, int[] arr) {
        Arrays.sort(arr);
        int min = Integer.MAX_VALUE;
        for(int j = 0; j < arr.length-k+1; j++){
            if(arr[j+k-1]-arr[j] < min){
                min = arr[j+k-1]-arr[j];
            }
        }
        System.out.println(min);
        return min;

        // Arrays.sort(arr);
        // List<Integer> tmp = new ArrayList<Integer>();
        // int min = Integer.MAX_VALUE;
        // for(int j = 0; j < arr.length-k; j++){
        //     for(int i = 0; i < k; i++){
        //         tmp.add(arr[i]);
        //     }
        //     if(tmp.get(tmp.size()-1) - tmp.get(0) < min){
        //         min = tmp.get(tmp.size()-1) - tmp.get(0);
        //     }
        // }
        // return min;



    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int k = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            int arrItem = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
            arr[i] = arrItem;
        }

        int result = maxMin(k, arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}

}
