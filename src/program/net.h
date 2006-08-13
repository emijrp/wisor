
//TODO
#define unicode(x,y) x

#include <string>
using namespace std;

extern class _net {
      SOCKET sockfd; 
      bool haysocket;
      void CreaSocket();
      void ServerConnect(const char* Server, const int Puerto=80);
      void SendRequest(const string& Request);
      void CierraSocket();  
     public: 
      _net();       
      ~_net();
      string pageText(const char* Servidor, const char* url);
      string inline pageText(const string& Servidor, const string& url) {
             return pageText(Servidor.c_str(), url.c_str()); }
      string trurl(const string& userinput);
      string fetch(const string& pagina,const string& project="es",const string& family="wikipedia");      
} net;
