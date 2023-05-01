"""
Nombre del fichero: contar_dedos.py
Autor: Francisco Manuel Villar Fernández
"""
# Importamos las librerías necesarias
import cv2
import mediapipe as mp


def hands_detection():
    # Importamos los módulos de Mediapipe necesarios
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # Capturamos
    cap = cv2.VideoCapture(0)

    # Iniciamos el módulo Hands
    with mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break

            # Convertimos la imagen de BGR a RGB 
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Procesamos la imagen con Mediapipe
            results = hands.process(image)

            total_fingers = 0

            # Dibujamos los puntos de referencia de las manos
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2),
                        mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2)
                    )

                    # Contamos los dedos de cada mano
                    thumb_up = False
                    index_up = False
                    middle_up = False
                    ring_up = False
                    pinky_up = False

                    # Pulgar
                    if hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y:
                        thumb_up = True

                    # Índice
                    if hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y:
                        index_up = True

                    # Corazón
                    if hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y:
                        middle_up = True

                    # Anular
                    if hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y:
                        ring_up = True

                    # Meñique
                    if hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y:
                        pinky_up = True

                    fingers_up = thumb_up + index_up + middle_up + ring_up + pinky_up

                    total_fingers += fingers_up

                    if hand_landmarks == results.multi_hand_landmarks[0]:
                        cv2.putText(image, f"Fingers (left hand): {fingers_up}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 0, 255), 2)
                    else:
                        cv2.putText(image, f"Fingers (right hand): {fingers_up}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 0, 255), 2)

            cv2.putText(image, f"Total fingers: {total_fingers}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Convertimos la imagen de RGB a BGR para mostrarla en la ventana
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Mostramos la imagen resultante
            cv2.imshow('MediaPipe Hands', image)

            if cv2.waitKey(5) & 0xFF == ord('q'):  # Apretamos 'q' para salir
                break

    # Liberamos los recursos
    cap.release()
    cv2.destroyAllWindows()


# Llamamos a la función principal
if __name__ == "__main__":
    hands_detection()
