import javax.swing.*;

public class ImageIcon1 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Text + Image Example");
        Icon icon = new ImageIcon("C:/Users/Dell/IdeaProjects/Java P1/src/images/background.jpg");
        JLabel label = new JLabel ("Java", icon, JLabel.RIGHT);

        label.setHorizontalTextPosition(JLabel.LEFT);
        label.setVerticalTextPosition(JLabel.CENTER);

        frame.add(label);
        frame.setSize(400,200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

    }
}
