#include <windows.h>
#include <wx/wx.h> 

#include "page.h"

class BoaApp : public wxApp {
    virtual bool OnInit();
};


class MyFrame: public wxFrame
{
public:

    MyFrame(const wxString& title, const wxPoint& pos, const wxSize& size);

    void OnQuit(wxCommandEvent& event);
    void OnAbout(wxCommandEvent& event);

    DECLARE_EVENT_TABLE()
};


enum
{
    ID_Quit = 1,
    ID_About,
};

BEGIN_EVENT_TABLE(MyFrame, wxFrame)
    EVT_MENU(ID_Quit, MyFrame::OnQuit)
//    EVT_MENU(ID_About, MyFrame::OnAbout)
END_EVENT_TABLE()

IMPLEMENT_APP(BoaApp)


bool BoaApp::OnInit()
{
    wxInitAllImageHandlers();
    MyFrame *main = new MyFrame( "Hello World", wxPoint(50,50), wxSize(450,340) );
    main->Show(TRUE);
    SetTopWindow(main);
    return TRUE;
} 

MyFrame::MyFrame(const wxString& title, const wxPoint& pos, const wxSize& size)
: wxFrame((wxFrame *)NULL, -1, title, pos, size)
{
                   /*
    application = BoaApp(0)
    application.MainLoop()*/                    

    CreateStatusBar();
    SetStatusText( "¡Bienvenido a Wisor!" );
}

void MyFrame::OnQuit(wxCommandEvent& WXUNUSED(event))
{
    Close(TRUE);
}
