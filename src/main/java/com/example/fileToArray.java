//copy n paste 1

package com.example;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**

The fileToArray class is used for importing data from a CSV file and storing it in an array.
@author (Your name)
@version (version number or date)
*/
public class fileToArray {
    void importToArr() {
        String csvFile = "fileInfo.csv";
        String line = "";
        String delim = ",";

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            while ((line = br.readLine()) != null) {
                String[] data = line.split(delim);
                for (String element : data) {
                    System.out.println(element);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
