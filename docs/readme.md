Função calculate_threshold

def calculate_threshold(gradient_magnitude, tolerance=1e-3, alpha=0.7):

	•	def calculate_threshold: Define a função chamada calculate_threshold, que será responsável por calcular um limiar adaptativo (threshold) para a imagem com base nas magnitudes dos gradientes.
	•	Parâmetros:
	•	gradient_magnitude: A matriz que contém os valores de magnitude dos gradientes da imagem.
	•	tolerance=1e-3: Um valor de tolerância (padrão é 0.001), que controla quando o algoritmo de thresholding iterativo deve parar. Ele define o quanto a mudança entre thresholds sucessivos deve ser pequena para encerrar a iteração.
	•	alpha=0.7: Um coeficiente de ajuste que afeta o valor inicial do limiar calculado. Esse parâmetro controla o grau de ajuste do threshold.



    T0 = np.max(gradient_magnitude)
    T1 = np.min(gradient_magnitude)

	•	T0 = np.max(gradient_magnitude): Calcula o valor máximo da magnitude do gradiente, ou seja, o maior valor de intensidade de gradiente encontrado na imagem.
	•	T1 = np.min(gradient_magnitude): Calcula o valor mínimo da magnitude do gradiente, ou seja, o menor valor de intensidade de gradiente.



    T_squared = (T0 * alpha) ** 2

	•	T_squared: Calcula o quadrado do valor ￼ (máximo gradiente) multiplicado pelo coeficiente ￼. Isso é parte da fórmula para ajustar o threshold de forma mais sensível à variação de gradientes.



    adapative_threshold = (T_squared + T1) / 2

	•	adapative_threshold: Define o threshold inicial como a média entre ￼ (o quadrado de ￼) e ￼ (o valor mínimo de gradiente). Esse valor inicial será ajustado iterativamente nas próximas etapas.

Laço While

    while True:

	•	while True:: Inicia um laço que será executado indefinidamente até que uma condição de parada seja atendida. Neste caso, a condição de parada será quando a mudança no threshold entre duas iterações consecutivas for menor que a tolerância definida.



        Ta_values = gradient_magnitude[gradient_magnitude >= adapative_threshold]
        Tb_values = gradient_magnitude[gradient_magnitude < adapative_threshold]

	•	Ta_values: Seleciona todos os valores de magnitude de gradiente que são maiores ou iguais ao threshold atual (adapative_threshold). Esses valores correspondem a áreas da imagem com gradientes mais fortes.
	•	Tb_values: Seleciona todos os valores de magnitude de gradiente que são menores que o threshold atual (adapative_threshold). Esses valores correspondem a áreas com gradientes mais fracos.



        Ta = np.mean(Ta_values) if len(Ta_values) > 0 else 0
        Tb = np.mean(Tb_values) if len(Tb_values) > 0 else 0

	•	Ta: Calcula a média dos valores de gradiente armazenados em Ta_values. Se Ta_values estiver vazio (não houver valores acima ou iguais ao threshold), Ta será definido como 0.
	•	Tb: Calcula a média dos valores de gradiente armazenados em Tb_values. Se Tb_values estiver vazio (não houver valores abaixo do threshold), Tb será definido como 0.



        new_T = (Ta + Tb) / 2

	•	new_T: Calcula um novo threshold como a média entre ￼ (a média dos gradientes fortes) e ￼ (a média dos gradientes fracos). Este novo threshold será usado na próxima iteração ou será o threshold final se atender à condição de parada.

Condição de Parada

        if abs(new_T - adapative_threshold) < tolerance:
            break

	•	if abs(new_T - adapative_threshold) < tolerance:: Se a diferença absoluta entre o novo threshold ￼ e o threshold adaptativo anterior for menor que a tolerância (definida como 0.001 por padrão), o laço while é interrompido, e o processo de iteração termina.
	•	break: Faz com que o laço while termine, indicando que o threshold convergiu para um valor final aceitável.



        adapative_threshold = new_T

	•	adapative_threshold = new_T: Atualiza o threshold adaptativo para o novo valor calculado ￼, para que ele possa ser usado na próxima iteração, se o laço while continuar.

Supressão de Gradientes Fracos

    gradient_magnitude[gradient_magnitude < adapative_threshold] = 0

	•	gradient_magnitude[gradient_magnitude < adapative_threshold] = 0: Todos os valores de magnitude do gradiente que são menores que o threshold final são definidos como zero. Isso efetivamente suprime gradientes fracos, preservando apenas os gradientes mais fortes que estão acima ou iguais ao threshold adaptativo final.

Retorno do Threshold Final

    return adapative_threshold

	•	return adapative_threshold: A função retorna o valor do threshold adaptativo final, que pode ser utilizado em outras partes do processo de detecção de bordas ou para análise posterior.


Função non_maximum_suppression

Esta função implementa a supressão de não máximos (Non-Maximum Suppression - NMS) com uma etapa adicional que divide a imagem em primeiro plano (foreground) e fundo (background), e aplica uma supressão adicional com base nas médias dessas duas regiões.


def non_maximum_suppression(mag, ang, width, height):
    suppressed = np.zeros((height, width), dtype=np.float64)

	•	def non_maximum_suppression: Define a função chamada non_maximum_suppression, que recebe como parâmetros a magnitude dos gradientes (mag), o ângulo dos gradientes (ang), e as dimensões da imagem (width e height).
	•	suppressed: Inicializa uma matriz de zeros com o mesmo tamanho da imagem para armazenar os valores suprimidos.



    ang = np.abs(ang)
    ang = np.where(ang > 180, np.abs(ang - 180), ang)

	•	ang = np.abs(ang): Converte os ângulos para valores absolutos, garantindo que os ângulos fiquem dentro do intervalo [0, 180] graus.
	•	ang = np.where(ang > 180, np.abs(ang - 180), ang): Ajusta qualquer ângulo maior que 180 graus para seu complemento, para garantir que o ângulo esteja no intervalo [0, 180].

Laço Principal: Verificação de Não-Máximos

    for i_y in range(1, height - 1):
        for i_x in range(1, width - 1):
            grad_ang = ang[i_y, i_x]

	•	for i_y in range(1, height - 1) e for i_x in range(1, width - 1): Laços que percorrem todos os pixels da imagem, excluindo as bordas.
	•	grad_ang = ang[i_y, i_x]: Obtém o valor do ângulo do gradiente para o pixel atual (em [i_y, i_x]).

Identificação dos Vizinhos com Base na Direção do Gradiente

Dependendo do valor do ângulo do gradiente, os vizinhos a serem comparados são selecionados. O código divide os ângulos em quatro faixas, correspondendo às direções principais:

            if grad_ang <= 22.5 or grad_ang > 157.5:
                neighb_1 = mag[i_y, i_x - 1]
                neighb_2 = mag[i_y, i_x + 1]

	•	Direção horizontal: Se o ângulo estiver perto de 0 ou 180 graus, os vizinhos são os pixels à esquerda e à direita.

            elif 22.5 < grad_ang <= 67.5:
                neighb_1 = mag[i_y - 1, i_x - 1]
                neighb_2 = mag[i_y + 1, i_x + 1]

	•	Direção diagonal descendente: Se o ângulo estiver entre 22.5 e 67.5 graus, os vizinhos são os pixels na diagonal superior esquerda e diagonal inferior direita.

            elif 67.5 < grad_ang <= 112.5:
                neighb_1 = mag[i_y - 1, i_x]
                neighb_2 = mag[i_y + 1, i_x]

	•	Direção vertical: Se o ângulo estiver entre 67.5 e 112.5 graus, os vizinhos são os pixels acima e abaixo.

            elif 112.5 < grad_ang <= 157.5:
                neighb_1 = mag[i_y + 1, i_x - 1]
                neighb_2 = mag[i_y - 1, i_x + 1]

	•	Direção diagonal ascendente: Se o ângulo estiver entre 112.5 e 157.5 graus, os vizinhos são os pixels na diagonal inferior esquerda e diagonal superior direita.

Supressão de Não-Máximos

            if mag[i_y, i_x] >= neighb_1 and mag[i_y, i_x] >= neighb_2:
                suppressed[i_y, i_x] = mag[i_y, i_x]
            else:
                suppressed[i_y, i_x] = 0

	•	Verificação de não-máximos: Se o valor do pixel atual for maior ou igual aos seus vizinhos (na direção do gradiente), ele é mantido no array suppressed. Caso contrário, ele é suprimido (definido como 0).

Segmentação em Primeiro Plano e Fundo

    foreground = suppressed[suppressed >= np.mean(suppressed)]
    background = suppressed[suppressed < np.mean(suppressed)]

	•	foreground: Define como “primeiro plano” todos os pixels cuja magnitude seja maior ou igual à média da matriz suppressed.
	•	background: Define como “fundo” todos os pixels cuja magnitude seja menor que a média.

Cálculo das Médias do Primeiro Plano e do Fundo

    foreground_mean = np.mean(foreground)
    background_mean = np.mean(background)

	•	foreground_mean: Calcula a média dos valores de magnitude do primeiro plano.
	•	background_mean: Calcula a média dos valores de magnitude do fundo.

Supressão Baseada nas Médias

    for i_y in range(1, height - 1):
        for i_x in range(1, width - 1):
            if suppressed[i_y, i_x] >= (foreground_mean + background_mean) / 2:
                suppressed[i_y, i_x] = suppressed[i_y, i_x]
            else:
                suppressed[i_y, i_x] = 0

	•	Segunda rodada de supressão: Percorre novamente a imagem e, para cada pixel, verifica se seu valor é maior ou igual à média entre o primeiro plano e o fundo. Se for, o valor é mantido, caso contrário, ele é suprimido (definido como 0).
	•	Esta etapa realiza uma segmentação mais precisa, eliminando gradientes mais fracos que não contribuem significativamente para a definição de bordas.

Retorno

    return suppressed

	•	return suppressed: Retorna a imagem final, onde apenas os pixels que correspondem a bordas proeminentes são mantidos, enquanto os demais são suprimidos.

Função modified_canny_detector

Essa função é uma versão modificada do detector de bordas Canny, incorporando uma série de modificações, como o uso de filtros Sobel personalizados, um filtro mediano, supressão de não-máximos e cálculo de limiar adaptativo.


def modified_canny_detector(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = apply_median_filter(img)

	•	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY): Converte a imagem de entrada, que está em formato colorido (BGR), para escala de cinza. Isso é necessário porque o detector de bordas trabalha melhor em uma imagem de canal único, como a imagem em tons de cinza.
	•	apply_median_filter(img): Aplica um filtro mediano na imagem em escala de cinza para suavizar a imagem e reduzir o ruído. O filtro mediano é particularmente útil para preservar as bordas enquanto remove pequenos ruídos.



    kernel_x, kernel_y = get_sobel_filters()
    grad_x = cv.filter2D(np.float64(img), cv.CV_64F, kernel_x)
    grad_y = cv.filter2D(np.float64(img), cv.CV_64F, kernel_y)

	•	kernel_x, kernel_y = get_sobel_filters(): Obtém os filtros Sobel personalizados (kernels) para calcular as derivadas da imagem nas direções X e Y. Esses filtros ajudam a detectar mudanças bruscas na intensidade, que são indicativas de bordas.
	•	grad_x = cv.filter2D(np.float64(img), cv.CV_64F, kernel_x): Aplica a convolução com o kernel Sobel na direção X, que retorna as mudanças de intensidade horizontal (bordas verticais).
	•	grad_y = cv.filter2D(np.float64(img), cv.CV_64F, kernel_y): Aplica a convolução com o kernel Sobel na direção Y, que retorna as mudanças de intensidade vertical (bordas horizontais).



    mag, ang = cv.cartToPolar(grad_x, grad_y, angleInDegrees=True)

	•	cv.cartToPolar(grad_x, grad_y, angleInDegrees=True): Converte as coordenadas cartesianas (derivadas nas direções X e Y) para coordenadas polares. Isso produz:
	•	mag: A magnitude do gradiente, que representa a intensidade da borda.
	•	ang: O ângulo do gradiente, que representa a direção da borda em graus.



    height, width = img.shape
    mag = non_maximum_suppression(mag, ang, width, height)

	•	height, width = img.shape: Obtém as dimensões da imagem (altura e largura).
	•	non_maximum_suppression(mag, ang, width, height): Aplica a supressão de não-máximos à magnitude do gradiente para afinar as bordas. A supressão de não-máximos remove todos os pixels que não são máximos locais na direção do gradiente, o que ajuda a garantir que apenas as bordas mais fortes sejam mantidas.



    adaptive_threshold = calculate_threshold(mag)

	•	calculate_threshold(mag): Calcula um threshold adaptativo com base na magnitude do gradiente. O threshold adaptativo determina qual valor de intensidade é suficiente para considerar um pixel como borda, ajustando-se dinamicamente de acordo com o conteúdo da imagem.



    _, binarized_image = cv.threshold(mag, adaptive_threshold, 255, cv.THRESH_BINARY)

	•	cv.threshold(mag, adaptive_threshold, 255, cv.THRESH_BINARY): Aplica o threshold adaptativo à magnitude do gradiente. Pixels com valores acima do threshold são definidos como 255 (branco), enquanto os outros são definidos como 0 (preto), resultando em uma imagem binarizada onde as bordas são destacadas.

