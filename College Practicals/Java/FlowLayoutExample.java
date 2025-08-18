import javax.swing.*;
import java.awt.*;

public class FlowLayoutExample {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Flow Layout Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,200);

        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout(FlowLayout.LEFT, 20 , 10));

        panel.add(new JLabel("Name:"));
        panel.add(new JTextField(10));

        panel.add(new JLabel("Email:"));
        panel.add(new JTextField(10));

        panel.add(new JButton("Submit"));
        frame.add(panel);
        frame.setVisible(true);
    }
}
