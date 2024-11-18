## Implementação do experimento de Renderização não Fotorrealista

### Grupo: André Carvalho, Caio Guilherme, Igor Cassimiro e Victor Macaúbas

### NPR Image Rendering

Este projeto implementa técnicas de Non-Photorealistic Rendering (NPR) para transformar imagens em estilos artísticos, como cartoon e pencil sketch. Ele utiliza conceitos como detecção de bordas, suavização com filtro bilateral, simplificação de cores e outras técnicas de processamento de imagens.

Requisitos

Certifique-se de ter os seguintes pacotes instalados:  
- Python
- Bibliotecas:
- OpenCV (opencv-python)
- NumPy (numpy)

### Como Rodar o Programa

	1.	Preparação:
	  •	Coloque as imagens que deseja processar na pasta input/.
	2.	Efeitos:
	  •	Para aplicar o efeito cartoon, execute o script a partir da pasta example/:

python run_npr_effects.py

	•	A saída será gerada na pasta output/.

### Estrutura do Projeto

O projeto está organizado em módulos para manter o código limpo e modular:

1. color_simplification/

	•	Contém funções para simplificar cores na imagem:
	•	posterization.py: Implementa a posterização para reduzir os níveis de cor.
	•	quantization.py: Usa K-Means para quantização adaptativa de cores.

2. edge_detection/

	•	Responsável pela detecção e processamento de bordas:
	•	canny_edge.py: Implementação customizada do algoritmo de Canny.
	•	filters.py: Funções para pré-processamento, como filtro mediano.
	•	gradient.py: Calcula gradientes com operadores Sobel.
	•	suppression.py: Supressão não máxima para refinar bordas.
	•	threshold.py: Cálculo adaptativo de limiares para detecção.

3. edge_stylization/

	•	Focado na estilização de bordas:
	•	edge_coloring.py: Colore as bordas com uma cor fixa ou com base na imagem original.
	•	line_width.py: Ajusta a largura das bordas de acordo com a intensidade.

4. npr_effects/

	•	Contém os efeitos NPR implementados:
	•	cartoon.py: Aplica o efeito cartoon usando suavização, simplificação de cores e bordas destacadas.
	•	pencil.py: Aplica o efeito pencil sketch, com suporte para texturas.

5. example/

	•	Scripts prontos para rodar e testar:
	•	run_npr_effects.py: Aplica os efeitos (cartoon ou sketch) nas imagens de entrada.
	•	improved_edge_detection.py: Demonstração apenas da detecção de bordas.

6. input/

	•	Pasta onde as imagens de entrada devem ser colocadas.

7. output/

	•	Pasta onde as imagens processadas serão salvas.

8. texture/

	•	Contém texturas para o efeito pencil sketch.

Exemplo de Uso

Imagem Original

Coloque sua imagem na pasta input/, por exemplo, input/sample_image.jpg.

Resultado do Cartoon

Após rodar os efeitos, a saída estará em output/
