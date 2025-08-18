import javax.swing.*;
import javax.swing.border.LineBorder;
import java.awt.*;

public class PanelDemo_Border {
    public static void main(String[] args) {
        JFrame frame = new JFrame("bordered JPanel");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500,500);

        JPanel panel = new JPanel();
        panel.setBackground(Color.GRAY);
        panel.setBorder(new LineBorder(Color.RED,5));
        frame.add(panel);
        frame.setVisible(true);
    }
}
