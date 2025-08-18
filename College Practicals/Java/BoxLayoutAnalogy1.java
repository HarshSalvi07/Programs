import javax.swing.*;
import java.awt.*;
public class BoxLayoutAnalogy1 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Bookshelf and Toolbox Layout");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,400);
        frame.setLayout(new GridLayout(1,2));

        JPanel bookshelfPanel = new JPanel();
        bookshelfPanel.setLayout(new BoxLayout(bookshelfPanel, BoxLayout.Y_AXIS));
        bookshelfPanel.setBorder(BorderFactory.createTitledBorder("Bookshelf"));

        bookshelfPanel.add(new JLabel("Java Programming"));
        bookshelfPanel.add(Box.createVerticalStrut(10));
        bookshelfPanel.add(new JLabel("Data Structures"));
        bookshelfPanel.add(Box.createVerticalStrut(10));
        bookshelfPanel.add(new JLabel("Operating Systems"));
        bookshelfPanel.add(Box.createVerticalStrut(10));
        bookshelfPanel.add(new JLabel("computer Networks"));

        JPanel toolboxPanel = new JPanel();
        toolboxPanel.setLayout(new BoxLayout(toolboxPanel, BoxLayout.X_AXIS));
        toolboxPanel.setBorder(BorderFactory.createTitledBorder("Toolbox"));

        toolboxPanel.add(Box.createHorizontalStrut(10));
        toolboxPanel.add(new JButton("wrench"));
        toolboxPanel.add(Box.createHorizontalStrut(10));
        toolboxPanel.add(new JButton("Hammer"));
        toolboxPanel.add(Box.createHorizontalStrut(10));
        toolboxPanel.add(new JButton("screwdriver"));
        toolboxPanel.add(Box.createHorizontalStrut(10));
        toolboxPanel.add(new JButton("Saw"));

        frame.add(bookshelfPanel);
        frame.add(toolboxPanel);
        frame.setVisible(true);
    }
}
