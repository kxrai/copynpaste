package com.example;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

/**
 * JavaFX App
 */
public class App extends Application {

    static Scene home;
    static Scene sec;

    @Override

    public void start(Stage stage) throws IOException {
        home = new Scene(loadFXML("homescreen"), 800, 480);
        stage.setScene(home);
        stage.show();
    }
    public void secondScreen(Stage stage) throws IOException {
        sec = new Scene(loadFXML("secondary"), 800, 480);
        stage.setScene(sec);
        stage.show();
    }
    

    static void setRoot(String fxml) throws IOException {
        home.setRoot(loadFXML(fxml));
        sec.setRoot(loadFXML(fxml));
    }

    private static Parent loadFXML(String fxml) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(App.class.getResource(fxml + ".fxml"));
        return fxmlLoader.load();
    }
    

    public static void main(String[] args) {
        launch();
    }
    

}