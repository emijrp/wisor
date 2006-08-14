
#include "net.h"
//Este contenido ya está en la clase net

inline vector<string> fetchQuery(const string& iniciales, const string& project, const string& family) {
       return net.fetchQuery(iniciales, project, family);
}

inline vector<string> pageQuery(const char* Servidor, const char* url) {
       return net.pageQuery(Servidor, url);
}

inline string trurlQuery(const string& userinput) {
       return net.trurl(userinput);
}
