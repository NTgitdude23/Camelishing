import zipfilefrom zipfile import BadZipfileimport sys , os , timeimport win32com.clientfrom messagebox import Messageclass EndCreate(object):    def __init__(self,mfile,saveas,url,text,textloc,buttontex,buttonloc,imgpath,imgloc):        try:            import xlsxwriter            print(mfile)            print(saveas)            excel = win32com.client.Dispatch("Excel.Application")            wb = excel.Workbooks.Add()            wb.SaveAs(mfile, FileFormat=52)            excel.Visible = False            time.sleep(3)            if os.path.isfile(mfile):                workbooktwo = excel.Workbooks.Open(Filename=mfile)                module = workbooktwo.VBProject.VBComponents.Add(1)                excel.Workbooks(1).Close(SaveChanges=1)                excel.Application.Quit()            else:                excel.Workbooks(1).Close(SaveChanges=0)                excel.Application.Quit()                sys.stderr.write("No File")                sys.stderr.flush()            workbook = xlsxwriter.Workbook(mfile)            worksheet = workbook.add_worksheet()            worksheet.set_column('A:A', 30)            worksheet.insert_image(imgloc, imgpath)            workbook.add_vba_project(saveas+"\\"+"vbaProject.bin")            worksheet.write(textloc, text)            worksheet.insert_button(buttonloc, {'macro': 'Crash',                'caption': buttontex,                'width': 80,                'height': 30})            workbook.close()            Message("Macro Creator", "Macro Create Successful !", "Finish !")        except Exception as f:            Message("Macro Creator", "Macro Create Unsuccessful !", "Error !")            t, o, tb = sys.exc_info()            print(f, tb.tb_lineno)class extractMacro(object):    def __init__(self,mfile,saveas,url,text,textloc,buttontex,buttonloc,imgpath,imgloc):        try:            filetype = ['.xls','.xlsx','.xlsm','.docx','.doc','.xlam','.xltx','.xlm','.xltm','.potm','.sldm']            extlist = []            esc = [filex for filex in filetype if mfile.endswith(filex) and extlist.append(filex)]            if not os.path.isfile(mfile):                sys.stderr.write("File Not Found")                sys.stderr.flush()                sys.exit()            elif not extlist:                sys.stderr.write("Unsupported Extension")                sys.stderr.flush()                sys.exit(0)            else:                pass            file = zipfile.ZipFile(mfile,mode="r")            info = file.namelist()            extract = list()            for i in info:                extract.append(i)            if "xl/vbaProject.bin" not in extract:                sys.stderr.write("Not Vba File !")                sys.stderr.flush()            else:                data = file.read('xl/vbaProject.bin')                with open(saveas+"\\"+"vbaProject.bin",mode="wb") as _:                    _.write(data)                    _.close()                    file.close()            os.remove(mfile)        except BadZipfile:            sys.stderr.write("Not Excel File")            sys.stderr.flush()        except Exception as f:            t, o, tb = sys.exc_info()            print(f, tb.tb_lineno)        EndCreate(mfile,saveas,url,text,textloc,buttontex,buttonloc,imgpath,imgloc)