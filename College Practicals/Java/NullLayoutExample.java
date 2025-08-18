import javax.swing.*;

public class NullLayoutExample {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Null Layout Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,300);

        JPanel panel = new JPanel();
        panel.setLayout(null);

        JLabel label = new JLabel("Enter Name");
        label.setBounds(30,30,100,25);
        panel.add(label);

        JTextField textField = new JTextField();
        textField.setBounds(140,30,150,25);
        panel.add(textField);

        JButton submitButton = new JButton("Enter");
        submitButton.setBounds(140,70,100,30);
        panel.add(submitButton);

        frame.add(panel);
        frame.setVisible(true);
    }
}
