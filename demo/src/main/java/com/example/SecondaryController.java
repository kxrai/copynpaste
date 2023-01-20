package com.example;

import java.io.IOException;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.text.Text;

public class SecondaryController {

    @FXML
    private Text PTFtitle;

    @FXML
    private Button backButton;

    @FXML
    private Text econTitle;

    @FXML
    private Text genflightTitle;

    @FXML
    void switchToSecondary(ActionEvent event) throws IOException {
        App.setRoot("homescreen");
    }

}
