package com.company;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


public class CatsAndAMouse {
    // Complete the catAndMouse function below.
    static String catAndMouse(int x, int y, int z) {
        int catA = x;
        int catB = y;
        int mouse = z;
        String ans = "";
        if(Math.abs(catA-mouse) == Math.abs(catB-mouse)){
            ans = "Mouse C";
        } else if (Math.abs(catA-mouse) < Math.abs(catB-mouse)){
            ans = "Cat A";
        } else if (Math.abs(catA-mouse) > Math.abs(catB-mouse)){
            ans = "Cat B";
        }
        return ans;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String[] xyz = scanner.nextLine().split(" ");

            int x = Integer.parseInt(xyz[0]);

            int y = Integer.parseInt(xyz[1]);

            int z = Integer.parseInt(xyz[2]);

            String result = catAndMouse(x, y, z);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}

}