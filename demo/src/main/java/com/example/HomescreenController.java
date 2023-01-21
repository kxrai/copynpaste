package com.example;

import java.io.FileWriter;
import java.io.IOException;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TextField;

public class HomescreenController {

    @FXML
    private TextField departCode;

    @FXML
    private TextField destCode;

    @FXML
    private DatePicker dstDate;

    @FXML
    private DatePicker homeDate;

    @FXML
    private Button searchButton;
    
    @FXML

    /* 
    public static void dateValidator (String[] args){
        DateTimeFormatter checkDate = DateTimeFormatter.ofPattern("yyyy-mm-dd");
        System.out.println(checkDate);
    }
    */

    void switchToSecondary(ActionEvent event) throws IOException {
        
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");

        //get first date
        String date1 = homeDate.getValue().format(formatter);
        System.out.println(date1);

        //get second date
        //System.out.println(dstDate.getValue());
        String date2 = dstDate.getValue().format(formatter);
        System.out.println(date2);

        // Airport Departure Code (Home Location)
        String dptCode = departCode.getText();
        // input validation to make sure user enters valid code
        if(dptCode.length()!=3 || !dptCode.matches("^[a-zA-Z]*$")){
            System.out.println("Enter valid airport code");
            return;
        }

        // Airport Departure Code (Destination)
        String dstCode = destCode.getText();
        // input validation to make sure user enters valid code
        if(dstCode.length()!=3 || !dstCode.matches("^[a-zA-Z]*$")){
            System.out.println("Enter valid airport code");
            return;
        }

        //String dptDate = departDate.getText();
        //String rtrDate = returnDate.getText();
        ArrayList<String> toPyarr = new ArrayList<String>();
        toPyarr.add(dptCode);
        toPyarr.add(dstCode);
        toPyarr.add(date1);
        toPyarr.add(date2);
        // toPyarr.add(dptDate);
        // toPyarr.add(rtrDate);
        FileWriter writer = new FileWriter("toPyScraper.txt"); 
        for(String str: toPyarr) {
        writer.write(str + System.lineSeparator());
        }
        writer.close();
        
        App.setRoot("secondary");
    }

}

