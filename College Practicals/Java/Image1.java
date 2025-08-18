import javax.swing.*;
import java.awt.*;

public class Image1 {
    public static void main(String[] args){
        JFrame frame = new JFrame("Image in JPanel - intelliJ");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600,400);

        JPanel imagePanel = new JPanel(){
          //  java.awt.Image backgroundImage = new ImageIcon((getClass().getResource("/images/Bats.png")).getImage());
            @Override
            protected void paintComponent(Graphics g){
                super.paintComponent(g);
               // g.drawImage(backgroundImage, 0, 0, getWidth(), getHeight(), this);
            }
        };
        frame.add(imagePanel);
        frame.setVisible(true);
    }
}
