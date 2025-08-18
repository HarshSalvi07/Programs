import javax.swing.*;
import java.awt.*;
public class PanelDemo3_Size {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Sized JPanel");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,500);
        frame.setLayout(null);

        JPanel panel = new JPanel();
        panel.setBackground(Color.PINK);
        panel.setBounds(50,50,200,200);

        frame.add(panel);
        frame.setVisible(true);
    }
}
