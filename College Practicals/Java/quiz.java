import javax.swing.*;
import java.awt.*;
public class quiz {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Colored JPanel");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,400);
        JPanel panel = new JPanel(new GridLayout(2, 2));
        for(int i = 1;i<=6;i++)
            panel.add(new JButton("Btn"+i));
        JPanel main = new JPanel(new BorderLayout());
        JPanel sub = new JPanel(new GridLayout(1, 2));
        sub.add(new JButton("X"));
        sub.add(new JButton("Y"));
        main.add(sub,BorderLayout.CENTER);

        frame.add(main);
        frame.setVisible(true);
    }
}
