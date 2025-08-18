import javax.swing.*;
import java.awt.*;

public class PanelDemo_Nested {
    public static void main(String[] args){
        JFrame frame = new JFrame("Nested Panels");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500,500);

        JPanel outerPanel = new JPanel();
        outerPanel.setLayout(new BorderLayout());
        outerPanel.setBackground(Color.GRAY);

        JPanel topPanel = new JPanel();
        topPanel.setBackground(Color.RED);
        topPanel.setPreferredSize(new Dimension(0,50));

        JPanel bottomPanel = new JPanel();
        bottomPanel.setBackground(Color.BLUE);
        bottomPanel.setPreferredSize(new Dimension(0,50));

        JPanel leftPanel = new JPanel();
        leftPanel.setBackground(Color.GREEN);
        leftPanel.setPreferredSize(new Dimension(80,0));

        JPanel rightPanel = new JPanel();
        rightPanel.setBackground(Color.ORANGE);
        rightPanel.setPreferredSize(new Dimension(80,0));

        JPanel centerPanel = new JPanel();
        centerPanel.setLayout(new FlowLayout());
        centerPanel.setBackground(Color.CYAN);

        JPanel nestedPanel = new JPanel();
        nestedPanel.setBackground(Color.MAGENTA);
        nestedPanel.setPreferredSize(new Dimension(100,50));
        centerPanel.add(nestedPanel);

        outerPanel.add(topPanel,BorderLayout.NORTH);
        outerPanel.add(bottomPanel,BorderLayout.SOUTH);
        outerPanel.add(leftPanel,BorderLayout.WEST);
        outerPanel.add(rightPanel,BorderLayout.EAST);
        outerPanel.add(centerPanel,BorderLayout.CENTER);

        frame.add(outerPanel);
        frame.setVisible(true);
    }
}

