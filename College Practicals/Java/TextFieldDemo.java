import javax.swing.*;
import java.awt.*;

public class TextFieldDemo {
    public static void main(String[] args) {
        JFrame frame = new JFrame("JTextField Demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,400);
        frame.setLayout(new FlowLayout());

        JTextField textField = new JTextField(10);
        frame.add(textField);

        String input = textField.getText();
        System.out.println("You typed:" + input);
        frame.setVisible(true);

    }
}
