import java.util.Scanner;
import java.util.Random;

public class Battleship 
{
	private static Scanner sc = new Scanner (System.in);
	
	private static String[][] tbl = new String[6][6];
	private static boolean[][] enemies = new boolean[6][6];
	
	public static void main (String[] args) 
	{
		
		System.out.println ("Bienvenido a Hundir la Flota.");
		System.out.println ("");
		
		menuPrincipal();
		
	}
	
	private static void menuPrincipal ()
	{
		System.out.println ("Selecciona una opcion:");
		System.out.println ("");
		System.out.println ("1 - Jugar");
		System.out.println ("2 - Instrucciones");
		System.out.println ("");
		
		boolean repeat = true;
		int selec = 0;
		
		do 
		{
			try
			{
				selec = sc.nextInt();
			}
			catch (Exception e)
			{
				System.out.println ("Introduce un carácter válido.");
			}
			
			if (selec != 1 & selec != 2)
			{
				System.out.println ("Introduce una opción válida.");
			}
			else
				repeat = false;
				
		} while (repeat);
		
		System.out.println ("");
		System.out.println ("");
		
		switch (selec) 
		{
			case 1: setGame(); break;
			case 2: menuInstrucciones(); break;
		}
		
	}
	
	private static void menuInstrucciones ()
	{
		System.out.println ("En cada turno tendras que decir la posicion que quieres atacar introduciendo las coordenadas siguiendo este formato: 'X.Y' donde X es la fila e Y la columna.");
		System.out.println ("Pulsa intro para volver al menu.");
		sc.nextLine();
		String s = sc.nextLine();
		limpiarPantalla();
		menuPrincipal();		
	}
	
	private static void setGame ()
	{
		Random randomGenerator = new Random();
		
		for (int x = 0; x < 6; x++)
		{
			for (int i = 0; i < 6; i++)
			{
				tbl[x][i] = "O";
			}
		}
		for (int x = 0; x < 6; x++)
		{
			for (int i = 0; i < 6; i++)
			{
				enemies[x][i] = false;
			}
		}
		for (int x = 0; x<4; x++)
		{
			if (Math.random() < 0.5f)
			{
				int file = randomGenerator.nextInt(6);
				int col = randomGenerator.nextInt(5);
			
				enemies[file][col] = true; enemies[file][col+1] = true;
			}
			else
			{
				int file = randomGenerator.nextInt(5);
				int col = randomGenerator.nextInt(6);
			
				enemies[file][col] = true; enemies[file+1][col] = true;
			}
		}
		
		int enemiesCount = 6;
		mainGame(enemiesCount);
	}
	
	private static void mainGame (int ec)
	{
		int shots = 0;
		do
		{
			showTable ();
			System.out.println ();
			sc.nextLine();
			System.out.println ("Ataca una posición (formato: X.Y):");
			String ps = sc.nextLine();
			
			try
			{
				int pos[] = new int[2];
				if (ps.charAt(0) == 'a')
					pos[1] = 0;
				else if (ps.charAt(0) == 'b')
					pos[1] = 1;
				else if (ps.charAt(0) == 'c')
					pos[1] = 2;
				else if (ps.charAt(0) == 'd')
					pos[1] = 3;
				else if (ps.charAt(0) == 'e')
					pos[1] = 4;
				else if (ps.charAt(0) == 'f')
					pos[1] = 5;
				else
				{
					System.out.println ("Introduce las coordenadas correctamente.");
					System.out.println ();
					continue;
				}
				
				pos[0] = (Character.getNumericValue(ps.charAt(2))-1);
				
				if (tbl[pos[0]][pos[1]] == "O")
				{
					if (enemies[pos[0]][pos[1]])
					{
						tbl[pos[0]][pos[1]] = "H";
						ec--;
						
						if (ec <= 0)
						{
							System.out.println ();
							showTable();
							System.out.println ();
							System.out.println ("Juego finalizado en " + shots + " intentos.");
							break;
						}
					}
					else
					{
						tbl[pos[0]][pos[1]] = "X";
					}
					shots++;
				}
				else
					System.out.println ("Ya has disparado a esta posición.");
			}	
			catch (Exception e)
			{
				System.out.println ("Introduce las coordenadas correctamente.");
			}		
		} while (true);
	}
	
	private static void showTable ()
	{
		for (int x = 0; x < 6; x++)
		{
			for (int i = 0; i < 6; i++)
			{
				System.out.print(tbl[x][i]);
			}
			System.out.println("");
		}
	}
	
	private static void limpiarPantalla ()
	{
		for (int x = 0; x<120; x++)
		{
			System.out.println ("");
		}
	}
	
}

