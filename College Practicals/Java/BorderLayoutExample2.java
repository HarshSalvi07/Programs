import javax.swing.*;
import java.awt.*;

public class BorderLayoutExample2 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Border Layout Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500,300);

        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout(10,10));

        panel.add(new JButton("North (Top)"),BorderLayout.NORTH);
        panel.add(new JButton("South (Bottom)"), BorderLayout.SOUTH);

        JPanel sidebar = new JPanel();
        sidebar.setLayout(new BoxLayout(sidebar,BoxLayout.Y_AXIS));
        sidebar.add(new JButton("Home"));
        sidebar.add(new JButton("profile"));
        sidebar.add(new JButton("Logout"));
        panel.add(sidebar, BorderLayout.WEST);

        panel.add(new JButton("East (Right)"), BorderLayout.EAST);
        panel.add(new JButton("Center (Main Area)"), BorderLayout.CENTER);

        frame.add(panel);
        frame.setVisible(true);
    }
}
