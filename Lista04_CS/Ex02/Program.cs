namespace Lista04_CS;

class Program 
{
    static void Main(string[] args)
    {
        Playlist = p new Playlist();
        p.SetNome("Rock")
        Musica m1 = new Musica();
        m1.SetNome = ("Musica 1");
        Musica m2 = new Musica();
        m2.SetNome("Musica 2")
        p.Inserir(m1);
        p.Inserir(m2);
        foreach (Musica m in p.listar())
            Console.WriteLine(m.GetNome())

    }
}