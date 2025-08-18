import javax.swing.*;


public class Window {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(()-> {
            JFrame frame = new JFrame();

            frame.setTitle("My Awesome JFrame Window");

            ImageIcon icon = new ImageIcon("images/Bats.png");
            frame.setIconImage(icon.getImage());

            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            frame.setSize(500, 400);

            frame.setLocationRelativeTo(null);
            frame.setResizable(false);
            frame.setVisible(true);
        });
    }
}
