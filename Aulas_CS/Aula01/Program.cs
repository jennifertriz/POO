// See https://aka.ms/new-console-template for more information
class MainClass {
    public static void Main() {
        Triangulo x = new Triangulo();
        x.SetBase(10);
        x.SetAltura(20);
        double area = x.CalcArea();
        Console.WriteLine(area);
    }
}
