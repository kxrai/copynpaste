package com.example;

import java.io.IOException;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.text.Text;

public class SecondaryController {

    @FXML
    private Text PTFtitle;

    @FXML
    private Text dptDateDestTxt;

    @FXML
    private Text dptDateHomeTxt;

    @FXML
    private Text econTitle;

    @FXML
    private Text genflightTitle;

    @FXML
    private Label opt1txt;

    @FXML
    private Label opt2txt;

    @FXML
    private Label opt3txt;

    @FXML
    private Label opt4txt;

    @FXML
    private Button primaryButton;

    @FXML
    void switchToSecondary(ActionEvent event) throws IOException {
        App.setRoot("homescreen");
    }

}
