package gui;

import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.input.MouseButton;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.CornerRadii;
import javafx.scene.paint.Color;
import javafx.stage.Stage;
import primitivos.AlgoritmosCirculos;
import primitivos.AlgoritmosRetas;
import primitivos.CirculoGr;
import primitivos.PontoGr;
import primitivos.RetaGr;

public class RetaComMouseGui  {
	int x1=0, y1=0, x2=0, y2=0;
	int x=0, y=0, xant=0, yant=0;

	boolean primeiraVez = true;

	public RetaComMouseGui(Stage palco) {

		// define titulo da janela
		palco.setTitle("Reta e Circulo com mouse");

		// define largura e altura da janela
		palco.setWidth(800);
		palco.setHeight(600);

		// Painel para os componentes
		BorderPane pane = new BorderPane();

		// componente para desenho
		Canvas canvas = new Canvas(800, 800);

		// componente para desenhar graficos
		GraphicsContext gc;
		gc = canvas.getGraphicsContext2D();

		// Eventos de mouse
		// trata mouseMoved
		canvas.setOnMouseMoved(event -> {
			palco.setTitle("(BotaoEsq - desenha reta) (BotaoDir - desenha circulo) (BotaoMeio - limpa canvas)"+" (" + (int)event.getX() + ", " + (int)event.getY() + ")");

		});

		// trata mousePressed
		canvas.setOnMousePressed(event -> {
			if (event.getButton() == MouseButton.PRIMARY) {
				if (primeiraVez == true) {
					x1 = (int)event.getX();
					y1 = (int)event.getY();
					new PontoGr(x1, y1, Color.BLUE, "", 6).desenharPonto(gc);
					primeiraVez = false;
				} else {
					x2 = (int)event.getX();
					y2 = (int)event.getY();
					RetaGr.desenhar(gc, x1, y1, x2, y2, "", Color.RED,  2, AlgoritmosRetas.MIDPOINT);					
					new PontoGr(x2, y2, Color.BLUE, "", 6).desenharPonto(gc);
					primeiraVez = true;
				}
			} else if(event.getButton() == MouseButton.SECONDARY) {
				if (primeiraVez == true) {
					x1 = (int)event.getX();
					y1 = (int)event.getY();
					new PontoGr(x1, y1, Color.BLUE, "", 6).desenharPonto(gc);
					primeiraVez = false;
				} else {
					x2 = (int)event.getX();
					y2 = (int)event.getY();
					double raio = new PontoGr (x1, y1).distance(x2, y2);
					CirculoGr.desenhar(gc, x1, y1, raio, Color.GREEN, "", 2, AlgoritmosCirculos.STROKELINE);					
					new PontoGr(x2, y2, Color.BLUE, "", 6).desenharPonto(gc);
					primeiraVez = true;
				}
			} else {
                gc.clearRect(0, 0, canvas.getWidth(), canvas.getHeight());

			}
			
			
		});


		// atributos do painel
		pane.setBackground(new Background(new BackgroundFill(Color.LIGHTGRAY, CornerRadii.EMPTY, Insets.EMPTY)));
		pane.setCenter(canvas); // posiciona o componente de desenho

		// cria e insere cena
		Scene scene = new Scene(pane);
		palco.setScene(scene);
		palco.show();	
	}

}
