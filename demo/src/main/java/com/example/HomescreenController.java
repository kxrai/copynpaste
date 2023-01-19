package com.example;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

public class HomescreenController {

    @FXML
    private TextField departCode;

    @FXML
    private TextField departDate;

    @FXML
    private TextField destCode;

    @FXML
    private TextField returnDate;

    @FXML
    private Button searchButton;

    @FXML
    void switchToSecondary(ActionEvent event) throws IOException {
        
        String dptCode = departCode.getText();
        String dptDate = departDate.getText();
        String dstCode = destCode.getText();
        String rtrDate = returnDate.getText();
        ArrayList<String> toPyarr = new ArrayList<String>();
        toPyarr.add(dptCode);
        toPyarr.add(dstCode);
        toPyarr.add(dptDate);
        toPyarr.add(rtrDate);
        FileWriter writer = new FileWriter("toPyScraper.txt"); 
        for(String str: toPyarr) {
        writer.write(str + System.lineSeparator());
        }
        writer.close();
        
        App.setRoot("secondary");
    }

}
