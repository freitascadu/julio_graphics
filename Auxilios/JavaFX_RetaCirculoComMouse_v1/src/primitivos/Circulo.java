package primitivos;

class Circulo{
	Ponto centro;
	double raio;

	Circulo(int x, int y, double raio){
		setCentro(new Ponto(x, y));
		setRaio(raio);  
	}
	Circulo(int x, int y, int raio){
		setCentro(new Ponto(x, y));
		setRaio(raio);  
	}
	Circulo(double x, double y, double raio){
		setCentro(new Ponto(x, y));
		setRaio(raio);  
	}
	Circulo(Ponto c, double raio){
		setCentro(new Ponto(c.getX(), c.getY()));
		setRaio(raio);  
	}

	Circulo(){
		setCentro(new Ponto(0,0));
		setRaio(0.0);  
	}

	void setRaio(double raio){
		this.raio = raio;
	}

	void setCentro(Ponto c){
		this.centro = c;
	}

	Ponto getCentro(){
		return centro;
	}

	double getRaio(){
		return raio;
	}

	public double calcularCircunferencia() {
		return(2*Math.PI*getRaio());
	}

	public double calcularArea() {
		return(Math.PI*Math.pow(getRaio(), 2));
	}

}