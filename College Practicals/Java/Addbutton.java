import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Addbutton {
    public static void main(String[] args) {
        JFrame frame = new JFrame("JButton Demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setLayout(new FlowLayout());

        JButton button = new JButton("Click Me!");
        button.setPreferredSize(new Dimension(120, 40));

        button.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent evt) {
                button.setBackground(Color.GREEN);
            }

            public void mousePressed(MouseEvent evt) {
                button.setBackground(Color.BLUE);
            }
        });

        frame.add(button);
        frame.setVisible(true);
    }
}