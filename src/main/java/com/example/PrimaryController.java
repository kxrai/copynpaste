package com.example;

import java.io.IOException;
import javafx.fxml.FXML;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

public class PrimaryController {

    @FXML
    private void switchToSecondary() throws IOException {
        App.setRoot("secondary");
    }
    /*
    *asks user for the arrival and departure location for the plane 
    *
    */
    public void start(Stage stage) {
      //Creating nodes
      TextField departureLoc = new TextField("Enter departure location");
      TextField arrivalLoc = new TextField("Enter arrival location");
      //Creating labels
      Label label1 = new Label("Departure Location");
      Label label2 = new Label("Arrival location: ");
      //Adding labels for nodes
      HBox box = new HBox(5);
      box.setPadding(new Insets(25, 5 , 5, 50));
      box.getChildren().addAll(label1, departureLoc, label2, arrivalLoc);
      //Setting the stage
      Scene scene = new Scene(box, 595, 150, Color.BEIGE);
      stage.setTitle("Text Field Example");
      stage.setScene(scene);
      stage.show();
        
        
      fileToArray run = new fileToArray ();
      run.importToArr();
   }


}
