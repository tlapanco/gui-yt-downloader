#Function to format seconds to hours:minutes:seconds in a string
def secs_ToHrsMinSec( secs ):
    horas=int()
    minutos=int()
    segundos=int()
    horas =secs//60//60
    minutos= secs//60-horas*60
    segundos = secs%60
    if horas < 10 : horas ='0'+str(horas)
    if minutos <10 : minutos = '0'+str(minutos)
    if segundos <10 : segundos= '0'+ str(segundos)
    secs_formato = str(horas)+":"+str(minutos)+":"+str(segundos)
    return secs_formato