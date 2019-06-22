def toggleState(st):
    file=open('misc/animation/state.txt','w')
    file.write(st)
    file.close()

def checkReadTextCondition(command):
    cmdCndt="اقراي" in command or "اقرء" in command or "اقراي" in command or "اقرا" in command
    cmdCndt=cmdCndt and "النص" in command
    return cmdCndt
def checkDateTextCondition(command):
    cmdCndt="تاريخ" in command and "اليوم" in command
    return cmdCndt
def checkSetAppointmentCondition(command):
    cmdCndt="\ufeffسجل" in command or "سجل" in command or "تسجيل" in command or "\ufeffتسجيل" in command or "سجلي" in command  or "تسجلي" in command or "حجز" in command 
    cmdCndt=cmdCndt and "موعد" in command or "موعدا" in command or "لقاء" in command 
    return cmdCndt
def checkGetAppointmentCondition(command):
    cmdCndt="هل" in command or "اليوم" in command 
    cmdCndt=cmdCndt and "موعد" in command or "موعدا" in command or "لقاء" in command 
    return cmdCndt
def checkCommunicationCondition(command):
    cmdCndt="تحدثي" in command or "تحدث" in command  or "تحدت" in command or "تكلمي" in command or "تكلمي" in command 
    cmdCndt=cmdCndt and "معي" in command or "مع" in command
    return cmdCndt
def checkSilence(command):
    cmdCndt= "اوسمتي" in command or "اصمتي" in command or "اسمتي" in command or "اسمطي" in command or "اسكتي" in command or "أريد" in command
    return cmdCndt
    
