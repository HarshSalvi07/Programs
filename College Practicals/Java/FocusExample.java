import javax.swing.*;
import java.awt.*;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;

public class FocusExample
{
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        JTextField textField = new JTextField();

        textField.addFocusListener(new FocusAdapter() {
            @Override
            public void focusGained(FocusEvent e) {
                System.out.println("Focused Gained");
            }
            public void focusLost(FocusEvent e) {
                System.out.println("Focused Lost");
            }
        });
        frame.add(textField);
        frame.setSize(300,150);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
    }

