import javax.swing.*;
import java.awt.*;

public class BoxLayoutExample {
    public static void main(String[] args) {
        JFrame frame = new JFrame("BoxLayout Example - Vertical List");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300,250);

        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel,BoxLayout.Y_AXIS));
        panel.setBorder(BorderFactory.createTitledBorder("Box Layout"));

        panel.add(new JButton("Dashboard"));
        panel.add(Box.createVerticalStrut(10));
        panel.add(new JButton("Profile"));
        panel.add(Box.createVerticalStrut(10));
        panel.add(new JButton("Settings"));
        panel.add(Box.createVerticalStrut(10));
        panel.add(new JButton("Logout"));

        frame.add(panel);
        frame.setVisible(true);
    }
}