import javax.swing.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class KeyExample{
    public static void main(String[] args){
        JFrame frame = new JFrame("Key Listner");
        JTextField textField = new JTextField();

        textField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                System.out.println("Key Pressed : "+e.getKeyChar());
            }
        });

        frame.add(textField);
        frame.setSize(300,300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
