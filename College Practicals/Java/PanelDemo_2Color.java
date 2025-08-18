import javax.swing.*;
import java.awt.*;
public class PanelDemo_2Color {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Colored JPanel");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,400);

        JPanel panel = new JPanel();
        panel.setBackground(Color.BLUE);

        frame.add(panel);
        frame.setVisible(true);
    }
}
