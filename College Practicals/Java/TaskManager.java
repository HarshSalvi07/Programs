import java.util.*;

abstract class Task{
    String title;

    Task(String title){
        this.title = title;
    }

    abstract void execute();
}

public class TaskManager {
    public static void main(String[] args) {
        List <Task>taskList = new ArrayList<>();

        //Task 1: Normal Task
        taskList.add(new Task("Buys Groceries"){
            void execute(){
                System.out.println("Task: "+title+" ✅ Done without hurry.");
            }
        });
        //Task 2: High Priority Task
        taskList.add(new Task("Pay Electricity Bill"){
            void execute(){
                System.out.println("Urgent Task: "+title+" ⚡ Complete.");
            }
        });

        //Task 3:
        taskList.add(new Task("Email Project Report"){
            void execute(){
                System.out.println("Task: "+title+" \uD83D\uDCC6 Scheduled and sent.");
            }
        });
        //Task 4: Very High Priority Task
        taskList.add(new Task("Attend Meeting"){
            void execute(){
                System.out.println("\uD83D\uDD34 Very Urgent Task: "+title+" \uD83C\uDFA4 Join Now.");
            }
        });
        //Execute all tasks
        System.out.println( "\n 📝 Executing Task List: \n");
        for(Task t:taskList){
            t.execute();
        }
    }
}
