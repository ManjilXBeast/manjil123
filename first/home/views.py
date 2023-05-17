from django.shortcuts import render,redirect
from . models import Student, Book
from . forms import StudentForm, BookForm , UserCreationForm
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')
# Create your views here.
def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def student(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'home/student.html',context)


def createstudent(request):
    if request.method =="GET":
        student_form = StudentForm
        return render(request, 'home/studentform.html', context = {'form':student_form})
    else:
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():
            student_form.save()
            return redirect('student')
    return render(request, 'home/studentform.html', context={'form':student_form})


def editstudent(request, student_id):   
    student = Student.objects.get(id = student_id)
    if request.method =='POST':
        form = StudentForm(instance = student)
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm(instance=student)
    return render(request, 'home/editstudent.html', context={'form': form})



def readstudent(request, student_id): 
    student = Student.objects.get(id = student_id)
    context={"student": student}
    return render(request, 'home/readstudent.html',context)



def deletestudent (request, student_id):
    student= Student.objects.get(id = student_id)
    if request.method =="POST":
        student.delete()
        return redirect('student')
    else:
        return render(request, 'home/deletestudent.html', {'student': student})

def bookindex(request):
    book = Book.objects.all()
    context ={'book': book}
    return render(request, 'book/index.html',context)

def createbook(request):
    if request.method =="GET":
        book_form = BookForm
        return render(request, 'book/create.html', context={'form': book_form})
    else:
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            book_form.save()
            return redirect('bookindex')
        return render(request, 'bookcreate.html', context={'form': book_form})
    
def editbook(request, book_id):
    book = Book.objects.get(id = book_id) 
    if request.method =="POST":
        book_form = BookForm(instance=book)
        book_form = BookForm(request.POST, request.FILES, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect('bookindex')
        else:
            book_Form = BookForm(instance=book)
            return render(request, 'book/update.html', {'form': book_form})
        

def home(request):
    return render(request,'home/index.html')

def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'auth/register.html', context={'form':form})

            