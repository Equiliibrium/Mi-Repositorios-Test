import cv2

def main():
    
    cap = cv2.VideoCapture(0)

   
    if not cap.isOpened():
        print("Error: No se pudo acceder a la cámara.")
        return

    print("Cámara iniciada. Presiona la tecla 'q' para salir.")

    
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error al capturar el cuadro. Saliendo...")
            break

        cv2.putText(frame, "Sistema Activo - Presiona Q para salir", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow('Detector de Somnolencia', frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()
    print("Programa finalizado correctamente.")


if __name__ == "__main__":
    main()
    
    
    
###