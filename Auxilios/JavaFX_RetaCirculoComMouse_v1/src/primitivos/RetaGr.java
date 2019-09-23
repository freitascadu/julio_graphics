package primitivos;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

public class RetaGr extends Reta{
	Color corReta;
	String nomeReta;
	int espessura;

	public RetaGr(int x1, int y1, int x2, int y2, Color corReta, String nomeReta, int espessura){
		super (x1, y1, x2, y2);
		setCorReta(corReta);
		setNomeReta(nomeReta);
		setEspessura(espessura);
	}    

	public RetaGr(int x1, int y1, int x2, int y2, Color corReta, int espessura){
		super (x1, y1, x2, y2);
		setCorReta(corReta);
		setNomeReta("");
		setEspessura(espessura);
	}   

	public RetaGr(int x1, int y1, int x2, int y2, int espessura){
		super (x1, y1, x2, y2);
		setCorReta(Color.BLACK);
		setNomeReta("");
		setEspessura(espessura);
	}   

	public RetaGr(PontoGr p1, PontoGr p2, int espessura){
		super(p1, p2);
		setCorReta(Color.BLACK);
		setNomeReta("");
		setEspessura(espessura);
	}    

	public RetaGr(PontoGr p1, PontoGr p2, Color corReta, int espessura){
		super(p1, p2);
		setCorReta(corReta);
		setNomeReta("");
		setEspessura(espessura);
	}    

	public RetaGr(PontoGr p1, PontoGr p2, Color corReta, String nomeReta, int espessura){
		super(p1, p2);
		setCorReta(corReta);
		setNomeReta(nomeReta);
		setEspessura(espessura);
	}    

	public void setCorReta(Color corReta) {
		this.corReta = corReta;
	}

	public void setNomeReta(String nomeReta) {
		this.nomeReta = nomeReta;
	}

	public Color getCor() {
		return corReta;
	}

	public String getStr() {
		return nomeReta;
	}
	/**
	 * @return the espessura
	 */
	public int getEsp() {
		return espessura;
	}

	/**
	 * @param espessura the espessura to set
	 */
	public void setEspessura(int espessura) {
		this.espessura = espessura;
	}

	//    public void desenharReta(Graphics g){
	private void desenharRetaEq(GraphicsContext g){

		double b=calculaB();
		double m=calculaM();

		//Caso 1) Caso em que o intervalo em y eh maior
		if(Math.abs(p2.getY()-p1.getY())>Math.abs(p2.getX()-p1.getX())){

			//Caso 1.1)Caso em que y1 > y2
			if(p1.getY()>p2.getY()){

				//System.out.println("Intervalo em Y eh maior com y1 > y2 .");
				if (p1.getX()==p2.getX()){
					PontoGr ponto=new PontoGr((int)p1.getX(),(int)p1.getY(),corReta,nomeReta, espessura);
					ponto.desenharPonto(g);
					for(double y=p2.getY();y<p1.getY();++y){
						ponto=new PontoGr((int)(p1.getX()),(int)y,corReta, espessura);
						ponto.desenharPonto(g);
					}
				}
				else{
					PontoGr ponto=new PontoGr((int)p2.getX(),(int)p2.getY(),corReta,nomeReta, espessura);
					ponto.desenharPonto(g);
					for(double y=p2.getY();y<p1.getY();++y){
						ponto=new PontoGr((int)((y-b)/m),(int)y,corReta, espessura);
						ponto.desenharPonto(g);
					}
				}

				//Caso 1.2)Caso em que x1 = x2
			}else if(p1.getX()==p2.getX()){

				//System.out.println("Intervalo em Y eh maior com Reta vertical .");
				PontoGr ponto=new PontoGr((int)p1.getX(),(int)p1.getY(),corReta,nomeReta, espessura);
				ponto.desenharPonto(g);
				for(double y=p1.getY();y<p2.getY();++y){
					ponto=new PontoGr((int)(p1.getX()),(int)y,corReta, espessura);
					ponto.desenharPonto(g);
				}
				//Caso 1.3)Caso em que y1 < y2  
			}else{

				//System.out.println("Intervalo em Y eh maior com x1 < x2 .");
				PontoGr ponto=new PontoGr((int)p1.getX(),(int)p1.getY(),corReta,nomeReta, espessura);
				ponto.desenharPonto(g);
				for(double y=p1.getY();y<p2.getY();++y){
					ponto=new PontoGr((int)((y-b)/m),(int)y,corReta, espessura);
					ponto.desenharPonto(g);
				}

			}

			//Caso 2)Caso em que o intervalo em x eh maior
		}else{

			//Caso 2.1)Caso em que x1 > x2
			if(p1.getX()>p2.getX()){

				//System.out.println("Intervalo em X eh maior com x1 > x2 .");
				PontoGr ponto=new PontoGr((int)p2.getX(),(int)p2.getY(),corReta,nomeReta, espessura);
				ponto.desenharPonto(g);
				for(double x=p2.getX();x<p1.getX();++x){
					ponto=new PontoGr((int)x,(int)(b+m*x),corReta, espessura);
					ponto.desenharPonto(g);
				}

				//Caso 2.2)Caso em que x1 = x2  
			}else if(p1.getX()==p2.getX()){

				//System.out.println("Intervalo em X eh maior com Reta Vertical .");
				PontoGr ponto=new PontoGr((int)p1.getX(),(int)p1.getY(),corReta,nomeReta, espessura);
				ponto.desenharPonto(g);
				for(double x=p1.getX();x<p2.getX();++x){
					ponto=new PontoGr((int)(p1.getX()),(int)(b+m*x),corReta, espessura);
					ponto.desenharPonto(g);
				}

				//Caso 2.3)Caso em que x1 < x2
			}else{

				//System.out.println("Intervalo em X eh maior com x1 < x2 .");
				PontoGr ponto=new PontoGr((int)p1.getX(),(int)p1.getY(),corReta,nomeReta, espessura);
				ponto.desenharPonto(g);
				for(double x=p1.getX();x<p2.getX();++x){
					ponto=new PontoGr((int)x,(int)(b+m*x),corReta, espessura);
					ponto.desenharPonto(g);
				}
			}
		}

	}

	private void desenharRetaDDA(GraphicsContext g){

		int x1 = (int)getP1().getX(), x2 = (int)getP2().getX();
		int y1 = (int)getP1().getY(), y2 = (int)getP2().getY();

		int dy = Math.abs(y2 - y1);
		int dx = Math.abs(x2 - x1);
		int  steps,  k;
		float xIncrement, yIncrement, x = x1, y = y1;

		if (Math.abs (dy) > Math.abs (dx)) {
			steps = Math.abs (dy);
		} else {
			steps = Math.abs (dx);
		}

		xIncrement = (float)dx / (float)steps;
		yIncrement = (float)dy / (float) steps;

		// para outros quadrantes
		if (y1 > y2) {
			yIncrement *= -1; 
		}
		if (x1 > x2) {
			xIncrement *= -1; 
		}

		PontoGr p0 = new PontoGr(Math.round (x), Math.round (y), corReta, espessura);
		p0.desenharPonto(g);

		for (k = 0; k < steps; k++) {
			x += xIncrement;
			y += yIncrement;
			p0 = new PontoGr(Math.round (x), Math.round (y), corReta, espessura);
			p0.desenharPonto(g);
		}
	}

	private void desenharRetaMidPoint(GraphicsContext g){

		int x1 = (int)getP1().getX(), x2 = (int)getP2().getX();
		int y1 = (int)getP1().getY(), y2 = (int)getP2().getY();
		int dx, dy, i, d;
		int incx, incy, inc1, inc2;
		int x,y;

		dx = x2-x1;
		dy = y2-y1;

		if (dx < 0) dx = -dx;
		if (dy < 0) dy = -dy;
		incx = 1;
		if (x2 < x1) incx = -1;
		incy = 1;
		if (y2 < y1) incy = -1;
		x = x1; y = y1;
		PontoGr ponto=new PontoGr(0,0,corReta,nomeReta, espessura);
		if (dx > dy) {
			ponto=new PontoGr(x,y,corReta,nomeReta, espessura);
			ponto.desenharPonto(g);
			d = 2 * dy-dx;
			inc1 = 2*(dy-dx);
			inc2 = 2*dy;
			for (i=0; i<dx; i++) {
				if (d >= 0) {
					y += incy;
					d += inc1;
				}
				else
					d += inc2;
				x += incx;
				ponto=new PontoGr(x,y,corReta,nomeReta, espessura);
				ponto.desenharPonto(g);
			}

		} else {
			ponto=new PontoGr(x,y,corReta,nomeReta, espessura);
			ponto.desenharPonto(g);
			d = 2*dx-dy;
			inc1 = 2*(dx-dy);
			inc2 = 2*dx;
			for (i=0; i<dy; i++) {
				if (d >= 0) {
					x += incx;
					d += inc1;
				}
				else
					d += inc2;
				y += incy;
				ponto=new PontoGr(x,y,corReta,nomeReta, espessura);
				ponto.desenharPonto(g);
			}
		}
	}

	private void desenharRetaStrokeLine(GraphicsContext g){
		g.setFill(getCor());
		g.setStroke(getCor());
		g.setLineWidth(getEsp());
		g.strokeLine(p1.getX(), p1.getY(), p2.getX(), p2.getY());
	}
	
	/**
	 * Desenha reta grafica 
	 * 
	 * @param g contexto grafico
	 * @param x1 x de P1
	 * @param y1 y de P1
	 * @param x2 x de P2
	 * @param y2 y de P2
	 * @param nome nome da reta
	 * @param cor cor do ponto
	 * @param esp espessura da reta
	 */
	public static void desenhar(GraphicsContext g, int x1, int y1, int x2, int y2, String nome, Color cor, int esp, AlgoritmosRetas alg) {
		RetaGr r; 

		// Cria um ponto
		r = new RetaGr(x1, y1, x2, y2, cor, nome, esp);

		// Desenha o ponto
		r.desenharReta(g, alg);
	}

	public static void desenhar(GraphicsContext g, double x1, double y1, double x2, double y2, String nome, Color cor, int esp, AlgoritmosRetas alg) {
		desenhar(g, (int)x1, (int) y1, (int) x2, (int) y2, nome, cor, esp, alg);
	}
	
	public void desenharReta(GraphicsContext g, AlgoritmosRetas alg) {
		if(alg == AlgoritmosRetas.EQUACAO) {
			desenharRetaEq(g);
		} else if (alg == AlgoritmosRetas.DDA) {
			desenharRetaDDA(g);
		} else if (alg == AlgoritmosRetas.MIDPOINT) {
			desenharRetaMidPoint(g);
		} else if (alg == AlgoritmosRetas.STROKELINE) {
			desenharRetaStrokeLine(g);
		}
	}
}