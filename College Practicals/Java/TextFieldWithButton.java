import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class TextFieldWithButton {
    public class TextFieldDemo{
        public static void main(String[] args) {
            JFrame frame = new JFrame("Login Example");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(400,400);
            frame.setLayout(new FlowLayout());

            JTextField nameField = new JTextField(20);
            JButton submit = new JButton("Submit");

            submit.addActionListener(e->{
                String name = nameField.getText();
                JOptionPane.showMessageDialog(frame,"Hello,"+name);

            });
            frame.add(new JLabel("Name:"));
            frame.add(nameField);
            frame.add(submit);

            frame.setVisible(true);
        }
    }
}
