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
import primitivos.PontoGr;

public class PontoComMouseGui  {
	int indicePonto=1;

	public PontoComMouseGui(Stage palco) {

		// define titulo da janela
		palco.setTitle("Testa Mouse");

		// define largura e altura da janela
		palco.setWidth(500);
		palco.setHeight(500);

		// Painel para os componentes
		BorderPane pane = new BorderPane();

		// componente para desenho
		Canvas canvas = new Canvas(500, 500);

		// componente para desenhar graficos
		
		GraphicsContext gc;
		gc = canvas.getGraphicsContext2D();

		// Eventos de mouse
		// trata mouseMoved
		canvas.setOnMouseMoved(event -> {
			palco.setTitle("Testa Mouse (Pressione botao do Mouse):"+" (" + (int)event.getX() + ", " + (int)event.getY() + ")");
		});

		// trata mousePressed
		canvas.setOnMousePressed(event -> {
			int x, y;

			if (event.getButton() == MouseButton.PRIMARY) {
				x = (int)event.getX();
				y = (int)event.getY();
				// desenha ponto na posicao clicada
				desenharPonto(gc, x, y, 4, "P"+indicePonto, Color.BLUE);
				indicePonto++;
			} else if (event.getButton() == MouseButton.SECONDARY) {
				x = (int)event.getX();
				y = (int)event.getY();
				// desenha ponto na posicao clicada
				desenharPonto(gc, x, y, 4, "("+ x + ", " + y +")", Color.RED);
			}
		});

		// atributos do painel
		pane.setBackground(new Background(new BackgroundFill(Color.AZURE, CornerRadii.EMPTY, Insets.EMPTY)));
		pane.setCenter(canvas); // posiciona o componente de desenho
		
		// cria e insere cena
		Scene scene = new Scene(pane);
		palco.setScene(scene);
		palco.show();	
	}

	/**
	 * Desenha um ponto grafico 
	 * 
	 * @param g contexto grafico
	 * @param x posicao x
	 * @param y posicao y
	 * @param diametro diametro do ponto
	 * @param nome nome do ponto
	 * @param cor cor do ponto
	 */
	public void desenharPonto(GraphicsContext g, int x, int y, int diametro, String nome, Color cor) {
		PontoGr p; 

		// Cria um ponto
		p = new PontoGr(x, y, cor, nome, diametro);

		// Desenha o ponto
		p.desenharPonto(g);
	}
}
