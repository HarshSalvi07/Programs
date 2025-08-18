import javax.swing.*;
public class PanelDemo_Simple {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Simple Panel");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,500);

        JPanel panel = new JPanel(); //Default layout = FlowLayout
        frame.add(panel); //add panel to frame
        frame.setVisible(true);
    }
}
