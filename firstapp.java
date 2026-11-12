import javax.swing.*;
class SwingDemo
{	
	SwingDemo()
	{	
		JFrame if=new JFrame("first App");
	}
public static void main(String args[])
{
SwingUtilities.invokelater(new runnable(
{ 
	public void run()
	{ 
 		new SwingDemo();
	}
});
}
}