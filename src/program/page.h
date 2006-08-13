
#include <string>
using namespace std;

#include "net.h"
#define self (*this)
class Page {
   string lang;
   string fam;
   string title;
   string contenido;
	
	public:
	//Clase para la gestión de las páginas de wikipedia, desde generar estadísticas chorras hasta
	//diferentes parseos del código wiki
	/*string changePage(char* titulo);
	string getText();
	size_t getLen();  // */
	//TODO: contar líneas
	//TODO: contar palabras
	//TODO: contar letras
	//TODO: cualquier otra estadística txorra
	//TODO: getTitle()
	//TODO: getNamespace() (tener cuidado con los diferentes idiomas)
	//TODO: parsearTexto (ufff)
	
	
	Page (const char* title="Portada", const char* lang="es", const char* fam="wikipedia") {
		self.lang=lang;
		self.fam=fam;
		self.title=title;
		self.contenido=net.fetch(self.title,self.lang,self.fam);
    }

	void changePage(const char* title) {
		self.title=title;
		self.contenido=net.fetch(self.title,self.lang,self.fam);
    }

	string getText() {
//		Devuelve el texto de la página en wikicódigo	
		return self.contenido;
    }

	size_t getLen() {
	//Devuelve el tamaño de la página
		return self.contenido.size();
    }
	
};
