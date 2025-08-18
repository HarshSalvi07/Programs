import javax.swing.*;
import java.awt.*;
public class BoxLayoutExamplee {
    public static void main(String[] args) {
        JFrame frame = new JFrame("BoxLayout - Vertical list");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,400);

        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel,BoxLayout.Y_AXIS));
        panel.setBorder(BorderFactory.createEmptyBorder(20,50,20,50));

        panel.add(new JButton("Dashboard"));
        panel.add(Box.createVerticalStrut(10));
        panel.add(new JButton("Profile"));
        panel.add(Box.createVerticalStrut(10));
        panel.add(new JButton("Settings"));
        panel.add(Box.createVerticalStrut(10));
        panel.add(new JButton("About"));

        frame.add(panel);
        frame.setVisible(true);
    }
}
