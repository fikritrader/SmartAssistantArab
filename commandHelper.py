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
    cmdCndt="\ufeffسجل" in command or "سجل" in command or "تسجيل" in command or "\ufeffتسجيل" in command or "سجلي" in command 
    cmdCndt=cmdCndt and "موعد" in command or "موعدا" in command or "لقاء" in command 
    return cmdCndt
def checkGetAppointmentCondition(command):
    cmdCndt="هل" in command or "اليوم" in command 
    cmdCndt=cmdCndt and "موعد" in command or "موعدا" in command or "لقاء" in command 
    return cmdCndt
