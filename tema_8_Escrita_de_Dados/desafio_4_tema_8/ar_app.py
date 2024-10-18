import arucolib
import cv2
import numpy as np

# Carregar o detector de marcadores AR
aruco = arucolib.Dictionary_get(arucolib.DICT_4X4_50)

# Carregar a câmera
cap = cv2.VideoCapture(0)

# Carregar uma imagem para sobreposição
overlay_image = cv2.imread('overlay.png')
# Redimensiona para o tamanho do marcador
overlay_image = cv2.resize(overlay_image, (100, 100))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Converter para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar os marcadores AR
    corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco)

    if ids is not None:
        # Desenhar os marcadores detectados
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        for corner in corners:
            # Calcular o centro do marcador
            x, y = corner[0].mean(axis=0).astype(int)

            # Sobrepor a imagem
            overlay_height, overlay_width, _ = overlay_image.shape
            start_x = x - overlay_width // 2
            start_y = y - overlay_height // 2
            end_x = start_x + overlay_width
            end_y = start_y + overlay_height

            # Garantir que as coordenadas estejam dentro dos limites da imagem
            start_x = max(0, start_x)
            start_y = max(0, start_y)
            end_x = min(frame.shape[1], end_x)
            end_y = min(frame.shape[0], end_y)

            # Adicionar a sobreposição
            frame[start_y:end_y, start_x:end_x] = cv2.addWeighted(
                frame[start_y:end_y, start_x:end_x], 0.5,
                overlay_image[0:(end_y-start_y), 0:(end_x-start_x)], 0.5, 0
            )

    # Exibir o resultado
    cv2.imshow('AR Application', frame)

    # Interromper o loop com a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
