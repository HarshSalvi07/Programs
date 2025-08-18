import javax.swing.*;
import java.awt.*;

public class BoxLayoutAnalogy {
   public static void main(String[] args) {
       JFrame frame = new JFrame();
       frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       frame.setSize(600,300);

       frame.setLayout(new GridLayout(1,2));

       JPanel bookshelfPanel = new JPanel();
       bookshelfPanel.setLayout(new BoxLayout(bookshelfPanel,BoxLayout.Y_AXIS));
       bookshelfPanel.setBorder(BorderFactory.createTitledBorder("Bookshelf"));

       bookshelfPanel.add(new JLabel(" Java Programming"));
       bookshelfPanel.add(Box.createVerticalStrut(10));
       bookshelfPanel.add(new JLabel("Data Structures"));
       bookshelfPanel.add(Box.createVerticalStrut(10));
       bookshelfPanel.add(new JLabel(" Operations"));
       bookshelfPanel.add(Box.createVerticalStrut(10));
       bookshelfPanel.add(new JLabel(" "));

   }

}
