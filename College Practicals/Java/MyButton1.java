import javax.swing.*;
import java.awt.*;

public class MyButton1 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("JButton Demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,200);

        JButton button = new JButton("Click Me");
        button.setBackground(Color.BLUE);
        button.setForeground(Color.WHITE);
        button.setFont(new Font("Arial", Font.BOLD, 16));
        button.setLayout(new FlowLayout());
        button.setFocusPainted(false);

        frame.add(button);

        frame.setVisible(true);
    }
}
