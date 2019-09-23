package primitivos;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

public class CirculoGr extends Circulo{
    Color cor;
    String str;
	int esp;

    public CirculoGr(int x, int y, double raio, Color cor, String str, int esp){
        super(x, y, raio);
        setCor(cor);
        setStr(str);
		setEsp(esp);
    }
    
    
    public CirculoGr(PontoGr c, double raio, Color cor, String str, int esp){
        super(c, raio);
        setCor(cor);
        setStr(str);
		setEsp(esp);
    }

    public CirculoGr(){
        super(new PontoGr(0, 0), 0.0);
        setCor(Color.BLACK);
		setEsp(0);
    }

    void setCor(Color cor){
        this.cor = cor;
    }

    Color getCor(){
        return this.cor;
    }
    private String getStr(){
        return this.str;
    }

    private void setStr(String str){
    	this.str = str;
    }

	/**
	 * @return the espessura
	 */
	public int getEsp() {
		return esp;
	}

	/**
	 * @param espessura the espessura to set
	 */
	public void setEsp(int esp) {
		this.esp = esp;
	}
	private void desenharCirculoPolar(GraphicsContext g){
    	g.setFill(Color.BLACK);
    	g.strokeText(getStr(),(int)getCentro().getX(), (int)getCentro().getY());
		g.setFill(getCor());
        g.setLineWidth(getEsp());
        desenharCirculo((int)getCentro().getX(),(int)getCentro().getY(),(int)getRaio(),g);
    }


    private void desenharCirculo(int cx, int cy, int raio, GraphicsContext g){
        if (raio != 0) {

            int x = 0;
            int y = raio;
            PontoGr p = new PontoGr(x, y, getCor(), getEsp());
            for (double alfa=0; alfa <= 45; alfa=alfa+0.2) {
                // Calcula um ponto e desenha os outros 7 por simetria.
                x=(int)(raio*Math.cos((alfa*Math.PI)/180.));
                y=(int)(raio*Math.sin((alfa*Math.PI)/180.));
                p = new PontoGr(cx+x, cy+y, getCor(), getEsp());
                p.desenharPonto(g);
                
                p = new PontoGr(cx+y, cy+x, getCor(), getEsp());
                p.desenharPonto(g);
                
                p = new PontoGr(cx+y, cy-x, getCor(), getEsp());
                p.desenharPonto(g);
                
                p = new PontoGr(cx+x, cy-y, getCor(), getEsp());
                p.desenharPonto(g);
                
                p = new PontoGr(cx-x, cy-y, getCor(), getEsp());
                p.desenharPonto(g);
                
                p = new PontoGr(cx-y, cy-x, getCor(), getEsp());
                p.desenharPonto(g);
                
                p = new PontoGr(cx-y, cy+x, getCor(), getEsp());
                p.desenharPonto(g);
                
                p = new PontoGr(cx-x, cy+y, getCor(), getEsp());
                p.desenharPonto(g);
            }
        }

    }

    private void desenharCirculoMidPoint(GraphicsContext g){
    	g.setFill(Color.BLACK);
    	g.strokeText(getStr(),(int)getCentro().getX(), (int)getCentro().getY());
		g.setFill(getCor());
        desenharCirculoMidPoint((int)getCentro().getX(),(int)getCentro().getY(),(int)getRaio(),g);
    }

    private void desenharCirculoMidPoint(int cx, int cy, int raio, GraphicsContext g) {

        if (raio != 0) {

            double x = 0;
            double y = raio;
            double d = 5 / 4 - raio;

            desenharPontos (cx, cy, (int)x, (int)y, g); // passa os pontos para serem desenhados

            while (y > x) {
                if (d < 0) {
                    d = d + 2 * x + 3;
                    x++;
                }
                
                else {
                    d = d + 2 * (x - y) + 5;
                    x++;
                    y--;
                }
                desenharPontos (cx, cy, (int)x, (int)y, g);
            }
        }       
    }

    //desenha os pontos passados pelo Bresenham para cada 1/8 do circulo
    private void desenharPontos(int x0, int y0, int x, int y, GraphicsContext g) {
        PontoGr p = new PontoGr(x0+x, y0+y, getCor());
        p.desenharPonto(g);
        p = new PontoGr(x0+y, y0+x, getCor(), getEsp());
        p.desenharPonto(g);
        p = new PontoGr(x0+y, y0-x, getCor(), getEsp());
        p.desenharPonto(g);
        p = new PontoGr(x0+x, y0-y, getCor(), getEsp());
        p.desenharPonto(g);
        p = new PontoGr(x0-x, y0-y, getCor(), getEsp());
        p.desenharPonto(g);
        p = new PontoGr(x0-y, y0-x, getCor(), getEsp());
        p.desenharPonto(g);
        p = new PontoGr(x0-y, y0+x, getCor(), getEsp());
        p.desenharPonto(g);
        p = new PontoGr(x0-x, y0+y, getCor(), getEsp());
        p.desenharPonto(g);
    }
    
	private void desenharCirculoStrokeOvall(GraphicsContext g){
		g.setFill(getCor());
        g.setStroke(getCor());
		g.setLineWidth(getEsp());
	    g.strokeOval((int)getCentro().getX()-(int)getRaio(), (int)getCentro().getY()-(int)getRaio(), 2*(int)getRaio(), 2*(int)getRaio());
	}
	
	public static void desenhar(GraphicsContext g, int x, int y, double raio, Color cor, String str, int esp, AlgoritmosCirculos alg) {
		CirculoGr c; 

		// Cria um ponto
		c = new CirculoGr (x, y, raio, cor, str, esp);

		// Desenha o ponto
		c.desenharCirculo(g, alg);
	}

	public static void desenhar(GraphicsContext g, double x1, double y1, double raio, Color cor, String str, int esp, AlgoritmosCirculos alg) {
		desenhar(g, (int)x1, (int) y1, raio, cor, str, esp, alg);
	}

	public void desenharCirculo(GraphicsContext g, AlgoritmosCirculos alg) {
		if (alg == AlgoritmosCirculos.POLAR) {
			desenharCirculoPolar(g);
		} else if (alg == AlgoritmosCirculos.MIDPOINT) {
			desenharCirculoMidPoint(g);
		} else if (alg == AlgoritmosCirculos.STROKELINE) {
			desenharCirculoStrokeOvall(g);
		}
	}
}
