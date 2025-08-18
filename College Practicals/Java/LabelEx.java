import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class LabelEx {
    public static void main(String[] args) {
        JFrame frame = new JFrame("JLabel demo by Mr Harsh");
        frame.setSize(300,200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel label = new JLabel("Hello Mr Harsh");
        label.setBounds(50,50,100,30); //X,Y,WIDTH,HEIGHT
        frame.setLayout(null); //Absolute positioning
        frame.add(label);

        frame.setVisible(true);

    }
}
