class MainClass {
    public static void Main() {
        Viagem x = new Viagem();
        x.SetDist(50);
        x.setTemp(0.5);
        double resultado = x.CalcVelocidade();
        Console.WriteLine($"A velocidade média da viagem é de {resultado} km/h!");
    }
}
