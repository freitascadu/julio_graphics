package primitivos;

import javafx.geometry.Point2D;

public class Ponto extends Point2D{

	Ponto (double x, double y) {
		super(x, y);
	}

	Ponto () {
		this(0, 0);
	}

	Ponto (Ponto p) {
		this(p.getx(), p.gety());
	}

	public double getx() {
		return getX();
	}

	public double gety() {
		return getY();
	}

    public double calcularDistancia(Ponto p) {
		return distance(p);
	}
    
    public double calcularDistancia(double x, double y) {
		return distance(x, y);
	}
}