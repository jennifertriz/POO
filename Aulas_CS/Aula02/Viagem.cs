class Viagem { 
    double dist, temp;

    public void SetDist(double v) {
        if (v > 0) dist = v;
    }

    public void setTemp(double v) {
        if (v > 0) temp = v;
    }

    public double GetDist() {
        return dist;
    }

    public double GetTemp() {
        return temp;
    }

    public double CalcVelocidade() {
        return dist / temp;
    }
}