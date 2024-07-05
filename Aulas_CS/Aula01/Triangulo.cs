class Triangulo {
    private double b, h;

    public void SetBase(double v) {
        if (v > 0) b = v;
    }

    public void SetAltura(double v) {
        if (v > 0) h = v; 
    }

    public double GetBase() {
        return b; 
    }

    public double GetAltura() {
        return h;
    }

    public double CalcArea() {
        return b * h / 2;
    }
}