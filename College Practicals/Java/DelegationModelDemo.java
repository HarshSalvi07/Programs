import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class DelegationModelDemo {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Event Handling Example");
        frame.setSize(300,200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JButton button = new JButton("Click Me");
        button.setBounds(100,70,100,40);

        button.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                JOptionPane.showMessageDialog(frame,"Click Me");
            }

        });
        frame.setLayout(null);
        frame.add(button);
        frame.setVisible(true);

    }
}
