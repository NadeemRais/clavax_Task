from django.shortcuts import render,redirect
from student.models import Student

# Create your views here.

def home(request):
    data = Student.objects.all()

    return render(request, 'home.html', {"data":data})

def addStudent(request):
    if request.method == 'POST':
        s_name1 = request.POST.get('s_name')
        f_name1 = request.POST.get('f_name')
        DOB1 = request.POST.get('DOB')
        address1 = request.POST.get('address')
        city1 = request.POST.get('city')
        state1 = request.POST.get('state')
        pin1 = request.POST.get('pin')
        phone_no1 = request.POST.get('phone_no')
        email1 = request.POST.get('email')
        marks1 = request.POST.get('marks')
        date_enrolled1 = request.POST.get('date_enrolled')

        student = Student(
                s_name=s_name1,
                f_name=f_name1,
                DOB=DOB1,
                email=email1,
                phone_no=phone_no1,
                address=address1,
                city=city1,
                state = state1,
                pin = pin1,
                marks= marks1,
                date_enrolled = date_enrolled1

            )

        
        # Validations  
        error_msg = None
        if not s_name1:
            error_msg = "Student Name is required"

        if not f_name1:
            error_msg = "Father Name is required"

        if not DOB1:
            error_msg = "Date of birth is required"

        if not address1:
            error_msg = "Address is required"

        if not city1:
            error_msg = "City Name is required"


        if not state1:
            error_msg = "State Name is required"


        if not pin1:
            error_msg = "Pin Number is required"
        elif len(pin1)<6:
            error_msg="Pin Number Must be 6 digit"    

        if not phone_no1:
            error_msg = "Phone Number is required"

        elif len(phone_no1)< 10:
            error_msg="Pin Number Must be 10 digit"      


        if not email1:
            error_msg = "Email Id is required" 

        if not marks1:
            error_msg = "Marks is required"  

        elif student.uniqueEmail():
            error_msg="Email Allready Exist"

        elif student.uniquePhone():
            error_msg="Phone Number allready Exist"        
                        


        if not error_msg:
            student.save()
            return redirect('/')
        else:    
            return render(request,'studentform.html',{"error":error_msg})

    else:        
        return render(request, 'studentform.html')    
 
def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'UpdateStudent.html', context) 

def saveUpdate(request,pk):
    student = Student.objects.get(id=pk)
    student.s_name = request.POST.get('s_name')
    student.f_name = request.POST.get('f_name')
    student.email = request.POST.get('email')
    student.DOB = request.POST.get('DOB')
    student.phone_no = request.POST.get('phone_no')
    student.address = request.POST.get('address')
    student.city = request.POST.get('city')
    student.state = request.POST.get('state')
    student.pin = request.POST.get('pin')
    student.marks = request.POST.get('marks')
    student.class_opted = request.POST.get('class_opted')
    student.date_enrolled = request.POST.get('date_enrolled')


    student.save()
    return redirect('/')    

