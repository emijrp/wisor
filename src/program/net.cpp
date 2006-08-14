#ifdef _WIN32
  #include <winsock.h>
#else
  #include <sys/types.h>
  #include <sys/socket.h>
  #include <netinet/in.h> //Para struct sockaddr_in
  #include <netdb.h> //Errores con gethostbyname() y struct addr_in
  
  #define SOCKET int
  #define closesocket close
  #define SOCKET_ERROR -1
  
#endif


#include "net.h"
#define CRLF "\r\n"

class _net net;

_net::_net() {
     #ifdef _WIN32
       {
            WSADATA dato;
           if (WSAStartup(MAKEWORD(1, 1), &dato) != 0) {
              fprintf(stderr, "WSAStartup failed.\n");
              exit(1);
           } 
       }
     #endif
     CreaSocket();
}

void _net::CreaSocket() {
     if (haysocket) return;              
     if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == (SOCKET)SOCKET_ERROR) {
            perror("socket");
            exit(1);
     }
     haysocket = true;
}

void _net::CierraSocket() {
    if (haysocket)         
        closesocket(sockfd);
    haysocket = false;
}    

_net::~_net() {
     CierraSocket();         
}         

void _net::ServerConnect(const char* Server, const int Puerto) {
     struct hostent *he;
     struct sockaddr_in their_addr; // información de la dirección de destino 
     
     if ((he = gethostbyname(Server)) == NULL) {  // obtener información de máquina 
            perror("gethostbyname");
            exit(1);
     }
     
     their_addr.sin_family = AF_INET;    // Ordenación de bytes de la máquina 
     their_addr.sin_port = htons(Puerto);  // short, Ordenación de bytes de la red 
     their_addr.sin_addr = *((struct in_addr *)he->h_addr);
     memset(&(their_addr.sin_zero), 8, 0);  // poner a cero el resto de la estructura   

     if (connect(sockfd, (struct sockaddr *)&their_addr, sizeof(struct sockaddr)) == SOCKET_ERROR) {
            perror("connect");
            exit(1);
     }     
          
}


string _net::fetch(const string& pagina,const string& project,const string& family) {      
	return pageText(project+"."+family+".org", string("http://")+project+"."+family+".org/w/index.php?title="+trurl(pagina)+"&action=raw");
}

void _net::SendRequest(const string& Request) {
    if (SOCKET_ERROR == send(sockfd, Request.c_str(), Request.size(), 0)) {
             perror("send");
             exit(1);
    }         
}


string _net::pageText(const char* Servidor, const char* url) { 
    string request=string("") + "GET " + url + " HTTP/1.0" CRLF
    "User-Agent: Wisor 0.01" CRLF
    "Host: " + Servidor + CRLF
    "Accept-Charset: utf-8" CRLF 
    "Connection: close" CRLF
    CRLF;
    CreaSocket();
    ServerConnect(Servidor);
    SendRequest(request);

    //Ok, esto debería mejorarse...
    string Cabeceras, text;
    char D; bool EnCabeceras (true);
    while(recv(sockfd, &D, 1, 0) > 0) 
        if (EnCabeceras) {
           Cabeceras.push_back(D);
           if ((D=='\n') &&
               (Cabeceras[Cabeceras.size()-2] == '\r') && 
               (Cabeceras[Cabeceras.size()-3] == '\n') &&
               (Cabeceras[Cabeceras.size()-4] == '\r'))
               EnCabeceras = false;
        } else            
            text.push_back(D);
        
    
    CierraSocket();
    return unicode(text,"utf-8");       
}

string _net::trurl(const string& userinput) {
      string escaped; 
      char CarEscapado[sizeof("%FF")];
      for (size_t i=0; i < userinput.size(); i++) 
          if ((userinput[i] < 'A') || 
             ((userinput[i] > 'Z') && (userinput[i] < 'a')) || 
             (userinput[i] > 'z')) {
              sprintf(CarEscapado, "%%%2X", userinput[i]);             
          } else
            escaped.push_back(userinput[i]);
             
      return escaped; 
}       

vector<string> _net::fetchQuery(const string& iniciales, const string& project, const string& family) {
   return pageQuery((project+"."+family+".org").c_str(), (string("http://")+project+"."+family+".org/w/query.php?what=allpages&aplimit=100&apnamespace=0&apfrom="+trurlQuery(iniciales)+"&apfilterredir=nonredirects&format=xml").c_str());
}   
                     
                     
#define OpenTitle "<title>"
#define CloseTitle "</title>"

vector<string> _net::pageQuery(const char* Servidor, const char* url) {               
           string Text = pageText(Servidor, url);
           vector<string> vec;
           char* R = (char*)Text.c_str();
           char* R2;
           while(R = strstr(R, OpenTitle)) {
                 R += sizeof(CloseTitle)-1;
                 R2 = strstr(R, CloseTitle);              
                 if(!R2) //No debería pasar. Cada <title> debe tener su </title>
                        break;
                 
                 R2[0] = '\0';
                 vec.push_back(R);
                 R = R2 + 1;
           }
           return vec;      
}
