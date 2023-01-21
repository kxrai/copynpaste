package com.example;

import java.io.FileWriter;
import java.io.IOException;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TextField;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class HomescreenController {

    @FXML
    private TextField departCode;

    @FXML
    private TextField destCode;

    @FXML
    private TextField distanceCode;

    @FXML
    private Text distanceLabel;
    
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
        String date1 = homeDate.getValue().format(formatter).toUpperCase();
        System.out.println(date1);

        //get second date
        //System.out.println(dstDate.getValue());
        String date2 = dstDate.getValue().format(formatter).toUpperCase();
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
        String dtCode = distanceCode.getText();

        //String dptDate = departDate.getText();
        //String rtrDate = returnDate.getText();
        ArrayList<String> toPyarr = new ArrayList<String>();
        toPyarr.add(dptCode);
        toPyarr.add(dstCode);
        toPyarr.add(date1);
        toPyarr.add(date2);
        toPyarr.add(dtCode);
        // toPyarr.add(dptDate);
        // toPyarr.add(rtrDate);
        FileWriter writer = new FileWriter("toPyScraper.txt"); 
        for(String str: toPyarr) {
        writer.write(str + System.lineSeparator());
        }
        writer.close();
        
        App.setRoot("secondary");
        FXMLLoader loader = new FXMLLoader(getClass().getResource("secondary.fxml"));
        Parent root = loader.load();
        
        //Establishes the stage
        Stage stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
        Scene scene = new Scene(root);
        stage.setScene(scene);
        stage.show();

    }

}

