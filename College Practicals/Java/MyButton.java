import javax.swing.*;
import java.awt.*;

public class MyButton {
    public static void main(String[] args){
        JFrame frame = new JFrame("JButton demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,400);

        JButton button = new JButton("Click");
        button.setBackground(Color.BLUE);
        button.setForeground(Color.RED);
        button.setFont(new Font("Arial",Font.BOLD,25));
        button.setFocusPainted(false);

        button.addMouseListener(new java.awt.event.MouseAdapter(){
            public void mouseEntered(java.awt.event.MouseEvent evt){
                button.setBackground(Color.GREEN);
            }
            public void mouseExited(java.awt.event.MouseEvent evt){
                button.setBackground(Color.BLUE);
            }

        });


        frame.add(button);

        frame.setVisible(true);
    }
}
