# SimplePyrint is a python print driver for linux and windows.
import platform

class SimplePyrint:
    def linuxPrint(self,path):
        import cups
        conn = cups.Connection()
        printers = conn.getPrinters()
        printer_name = printers.keys()[0]
        conn.printFile(printer_name,path,"Receipt Printing", {})
        return

    def windowsPrint(self,path):
        import win32api
        win32api.ShellExecute(
            0,
            'print',
            path,
            None,
            '.',
            0
        )
        return

    def sPrint(self,path):
        if self.osType =='Windows':
            #path = string.replace(path,'/','//') # this may not be needed.
            self.windowsPrint(path)
            return
        if self.osType == 'Linux':
            self.linuxPrint(path)
            return

        print "Your OS is not supported"
        return

    def __init__(self):
        self.osType = platform.system()
        print self.osType
