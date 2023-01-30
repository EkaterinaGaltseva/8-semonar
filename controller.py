import view
import model


def start():
    model.GetLastStudentId()
    stop = False
    while not stop:
        model.SaveStudents()
        if view.GetNewStudentInfo('"q" to stop').lower() == 'q':
            stop = True

    model.SaveLastStudentId()