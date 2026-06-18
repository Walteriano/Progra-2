

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define pasos 10        
#define variacion 0.01f   

/*Estructura Eslabon*/
typedef struct {
    int identitificador;
    float posicionX;
    float posicionY;
} Eslabon;

/*Generación de Posición Inicial*/
void generarPosicionInicial(float *x, float *y) {
    *x = (rand() % 36001) / 100.0f; 
    *y = (rand() % 36001) / 100.0f; 
}

/*Simulación Avance*/
bool autoHome(Eslabon *e) {
    float pasoX = e->posicionX / pasos;
    float pasoY = e->posicionY / pasos;
    int contador = 0;

    printf("\nEslabon %d: posicion inicial (X=%.2f, Y=%.2f)\n", e->identitificador, e->posicionX, e->posicionY);

    while (e->posicionX != 0.0f || e->posicionY != 0.0f) {
        if (e->posicionX != 0.0f) {
            e->posicionX -= pasoX;
        }
        if (e->posicionY != 0.0f) {
            e->posicionY -= pasoY;
        }
        contador++;

        
        if (e->posicionX < variacion && e->posicionX > -variacion) e->posicionX = 0.0f;
        if (e->posicionY < variacion && e->posicionY > -variacion) e->posicionY = 0.0f;

        printf("  Paso %d -> X=%.2f, Y=%.2f\n", contador, e->posicionX, e->posicionY);
    }

    return (e->posicionX == 0.0f && e->posicionY == 0.0f);
}

int main() {
    srand((unsigned int) time(NULL));

    printf("Inicio de Simulación\n");
    

    
    Eslabon id1, id2, id3, id4;
    id1.identitificador = 1;
    id2.identitificador = 2;
    id3.identitificador = 3;
    id4.identitificador = 4;

    
    generarPosicionInicial(&id1.posicionX, &id1.posicionY);
    generarPosicionInicial(&id2.posicionX, &id2.posicionY);
    generarPosicionInicial(&id3.posicionX, &id3.posicionY);
    generarPosicionInicial(&id4.posicionX, &id4.posicionY);

    
    bool home1 = autoHome(&id1);
    if (home1) printf("Eslabon 1 terminado\n");

    bool home2 = autoHome(&id2);
    if (home2) printf("Eslabon 2 terminado\n");

    bool home3 = autoHome(&id3);
    if (home3) printf("Eslabon 3 terminado\n");

    bool home4 = autoHome(&id4);
    if (home4) printf("Eslabon 4 terminado\n");

    if (home1 && home2 && home3 && home4) {
        printf("Todos los eslabones realizaron auto-home correctamente.\n");
    }

    return 0;
}