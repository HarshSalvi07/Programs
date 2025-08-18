import javax.swing.*;
import java.awt.*;
public class ChessBoard {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Chess Board");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400,400);

        JPanel board = new JPanel(new GridLayout(8,8));

        for(int row = 0; row < 8; row++) {
            for(int col = 0; col < 8; col++) {
                JLabel square = new JLabel();
                square.setOpaque(true);

                if((row + col)%2==0) {
                    square.setBackground(Color.WHITE);
                }else{
                    square.setBackground(Color.BLACK);
                }
                board.add(square);
            }
        }
        frame.add(board);
        frame.setVisible(true);
    }
}
