import json
import os

from django.contrib import messages
from django.core.files.storage import FileSystemStorage  # To upload Profile Picture
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from student_management_app.forms import EditStudentForm, AddStudentForm
from student_management_app.models import CustomUser, Staffs, Courses, Subjects, Students, SessionYearModel, Attendance, \
    AttendanceReport, LeaveReportStaff, FeedBackStaffs, StudentResult, FirmwareUpload, ExecutableUpload


def staff_home(request):
    return render(request, "staff_template/staff_home_template.html", None)


# def staff_take_attendance(request):
#     subjects = Subjects.objects.filter(staff_id=request.user.id)
#     session_years = SessionYearModel.objects.all()
#     context = {
#         "subjects": subjects,
#         "session_years": session_years
#     }
#     return render(request, "staff_template/take_attendance_template.html", context)
#
#
# def staff_apply_leave(request):
#     staff_obj = Staffs.objects.get(admin=request.user.id)
#     leave_data = LeaveReportStaff.objects.filter(staff_id=staff_obj)
#     context = {
#         "leave_data": leave_data
#     }
#     return render(request, "staff_template/staff_apply_leave_template.html", context)
#
#
# def staff_apply_leave_save(request):
#     if request.method != "POST":
#         messages.error(request, "Invalid Method")
#         return redirect('staff_apply_leave')
#     else:
#         leave_date = request.POST.get('leave_date')
#         leave_message = request.POST.get('leave_message')
#
#         staff_obj = Staffs.objects.get(admin=request.user.id)
#         try:
#             leave_report = LeaveReportStaff(staff_id=staff_obj, leave_date=leave_date, leave_message=leave_message, leave_status=0)
#             leave_report.save()
#             messages.success(request, "Applied for Leave.")
#             return redirect('staff_apply_leave')
#         except:
#             messages.error(request, "Failed to Apply Leave")
#             return redirect('staff_apply_leave')


# def staff_feedback(request):
#     staff_obj = Staffs.objects.get(admin=request.user.id)
#     feedback_data = FeedBackStaffs.objects.filter(staff_id=staff_obj)
#     context = {
#         "feedback_data":feedback_data
#     }
#     return render(request, "staff_template/staff_feedback_template.html", context)
#
#
# def staff_feedback_save(request):
#     if request.method != "POST":
#         messages.error(request, "Invalid Method.")
#         return redirect('staff_feedback')
#     else:
#         feedback = request.POST.get('feedback_message')
#         staff_obj = Staffs.objects.get(admin=request.user.id)
#
#         try:
#             add_feedback = FeedBackStaffs(staff_id=staff_obj, feedback=feedback, feedback_reply="")
#             add_feedback.save()
#             messages.success(request, "Feedback Sent.")
#             return redirect('staff_feedback')
#         except:
#             messages.error(request, "Failed to Send Feedback.")
#             return redirect('staff_feedback')


# WE don't need csrf_token when using Ajax
# @csrf_exempt
# def get_students(request):
#     # Getting Values from Ajax POST 'Fetch Student'
#     subject_id = request.POST.get("subject")
#     session_year = request.POST.get("session_year")
#
#     # Students enroll to Course, Course has Subjects
#     # Getting all data from subject model based on subject_id
#     subject_model = Subjects.objects.get(id=subject_id)
#
#     session_model = SessionYearModel.objects.get(id=session_year)
#
#     students = Students.objects.filter(course_id=subject_model.course_id, session_year_id=session_model)
#
#     # Only Passing Student Id and Student Name Only
#     list_data = []
#
#     for student in students:
#         data_small={"id":student.admin.id, "name":student.admin.first_name+" "+student.admin.last_name}
#         list_data.append(data_small)
#
#     return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)
#
#
#
#
# @csrf_exempt
# def save_attendance_data(request):
#     # Get Values from Staf Take Attendance form via AJAX (JavaScript)
#     # Use getlist to access HTML Array/List Input Data
#     student_ids = request.POST.get("student_ids")
#     subject_id = request.POST.get("subject_id")
#     attendance_date = request.POST.get("attendance_date")
#     session_year_id = request.POST.get("session_year_id")
#
#     subject_model = Subjects.objects.get(id=subject_id)
#     session_year_model = SessionYearModel.objects.get(id=session_year_id)
#
#     json_student = json.loads(student_ids)
#     # print(dict_student[0]['id'])
#
#     # print(student_ids)
#     try:
#         # First Attendance Data is Saved on Attendance Model
#         attendance = Attendance(subject_id=subject_model, attendance_date=attendance_date, session_year_id=session_year_model)
#         attendance.save()
#
#         for stud in json_student:
#             # Attendance of Individual Student saved on AttendanceReport Model
#             student = Students.objects.get(admin=stud['id'])
#             attendance_report = AttendanceReport(student_id=student, attendance_id=attendance, status=stud['status'])
#             attendance_report.save()
#         return HttpResponse("OK")
#     except:
#         return HttpResponse("Error")
#
#
#
#
# def staff_update_attendance(request):
#     subjects = Subjects.objects.filter(staff_id=request.user.id)
#     session_years = SessionYearModel.objects.all()
#     context = {
#         "subjects": subjects,
#         "session_years": session_years
#     }
#     return render(request, "staff_template/update_attendance_template.html", context)
#
# @csrf_exempt
# def get_attendance_dates(request):
#
#
#     # Getting Values from Ajax POST 'Fetch Student'
#     subject_id = request.POST.get("subject")
#     session_year = request.POST.get("session_year_id")
#
#     # Students enroll to Course, Course has Subjects
#     # Getting all data from subject model based on subject_id
#     subject_model = Subjects.objects.get(id=subject_id)
#
#     session_model = SessionYearModel.objects.get(id=session_year)
#
#     # students = Students.objects.filter(course_id=subject_model.course_id, session_year_id=session_model)
#     attendance = Attendance.objects.filter(subject_id=subject_model, session_year_id=session_model)
#
#     # Only Passing Student Id and Student Name Only
#     list_data = []
#
#     for attendance_single in attendance:
#         data_small={"id":attendance_single.id, "attendance_date":str(attendance_single.attendance_date), "session_year_id":attendance_single.session_year_id.id}
#         list_data.append(data_small)
#
#     return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)
#
#
# @csrf_exempt
# def get_attendance_student(request):
#     # Getting Values from Ajax POST 'Fetch Student'
#     attendance_date = request.POST.get('attendance_date')
#     attendance = Attendance.objects.get(id=attendance_date)
#
#     attendance_data = AttendanceReport.objects.filter(attendance_id=attendance)
#     # Only Passing Student Id and Student Name Only
#     list_data = []
#
#     for student in attendance_data:
#         data_small={"id":student.student_id.admin.id, "name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name, "status":student.status}
#         list_data.append(data_small)
#
#     return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)
#
#
# @csrf_exempt
# def update_attendance_data(request):
#     student_ids = request.POST.get("student_ids")
#
#     attendance_date = request.POST.get("attendance_date")
#     attendance = Attendance.objects.get(id=attendance_date)
#
#     json_student = json.loads(student_ids)
#
#     try:
#
#         for stud in json_student:
#             # Attendance of Individual Student saved on AttendanceReport Model
#             student = Students.objects.get(admin=stud['id'])
#
#             attendance_report = AttendanceReport.objects.get(student_id=student, attendance_id=attendance)
#             attendance_report.status=stud['status']
#
#             attendance_report.save()
#         return HttpResponse("OK")
#     except:
#         return HttpResponse("Error")


def staff_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    staff = Staffs.objects.get(admin=user)

    context={
        "user": user,
        "staff": staff
    }
    return render(request, 'staff_template/staff_profile.html', context)


def staff_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('staff_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            staff = Staffs.objects.get(admin=customuser.id)
            staff.address = address
            staff.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('staff_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('staff_profile')


#
# def staff_add_result(request):
#     subjects = Subjects.objects.filter(staff_id=request.user.id)
#     session_years = SessionYearModel.objects.all()
#     context = {
#         "subjects": subjects,
#         "session_years": session_years,
#     }
#     return render(request, "staff_template/add_result_template.html", context)
#
#
# def staff_add_result_save(request):
#     if request.method != "POST":
#         messages.error(request, "Invalid Method")
#         return redirect('staff_add_result')
#     else:
#         student_admin_id = request.POST.get('student_list')
#         assignment_marks = request.POST.get('assignment_marks')
#         exam_marks = request.POST.get('exam_marks')
#         subject_id = request.POST.get('subject')
#
#         student_obj = Students.objects.get(admin=student_admin_id)
#         subject_obj = Subjects.objects.get(id=subject_id)
#
#         try:
#             # Check if Students Result Already Exists or not
#             check_exist = StudentResult.objects.filter(subject_id=subject_obj, student_id=student_obj).exists()
#             if check_exist:
#                 result = StudentResult.objects.get(subject_id=subject_obj, student_id=student_obj)
#                 result.subject_assignment_marks = assignment_marks
#                 result.subject_exam_marks = exam_marks
#                 result.save()
#                 messages.success(request, "Result Updated Successfully!")
#                 return redirect('staff_add_result')
#             else:
#                 result = StudentResult(student_id=student_obj, subject_id=subject_obj, subject_exam_marks=exam_marks, subject_assignment_marks=assignment_marks)
#                 result.save()
#                 messages.success(request, "Result Added Successfully!")
#                 return redirect('staff_add_result')
#         except:
#             messages.error(request, "Failed to Add Result!")
#             return redirect('staff_add_result')
#
#
# def staff_manage_student(request):
#     # Ensure only staff can access
#     # if not hasattr(request.user, 'staffs'):
#     #     return redirect('staff_home')
#     students = Students.objects.all()
#     context = {
#         "students": students
#     }
#     return render(request, 'staff_template/manage_student_template.html', context)
#
#
# def staff_edit_student(request, student_id):
#     # Ensure only staff can access
#     # if not hasattr(request.user, 'staffs'):
#     #     return redirect('staff_home')
#
#     # Add your edit student logic here
#     # This would be similar to HodViews.edit_student but for staff access
#     # pass
#     # Adding Student ID into Session Variable
#     request.session['student_id'] = student_id
#
#     student = Students.objects.get(admin=student_id)
#     form = EditStudentForm()
#     # Filling the form with Data from Database
#     form.fields['email'].initial = student.admin.email
#     form.fields['username'].initial = student.admin.username
#     form.fields['first_name'].initial = student.admin.first_name
#     form.fields['last_name'].initial = student.admin.last_name
#     form.fields['address'].initial = student.address
#     form.fields['course_id'].initial = student.course_id.id
#     form.fields['gender'].initial = student.gender
#     form.fields['session_year_id'].initial = student.session_year_id.id
#
#     context = {
#         "id": student_id,
#         "username": student.admin.username,
#         "form": form
#     }
#     return render(request, "staff_template/edit_student_template.html", context)
#
# def staff_add_student(request):
#     form = AddStudentForm()
#     context = {
#         "form": form
#     }
#     return render(request, 'staff_template/add_student_template.html', context)
#
#
#
# def staff_add_student_save(request):
#     if request.method != "POST":
#         messages.error(request, "Invalid Method")
#         return redirect('staff_add_student')
#     else:
#         form = AddStudentForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             address = form.cleaned_data['address']
#             session_year_id = form.cleaned_data['session_year_id']
#             course_id = form.cleaned_data['course_id']
#             gender = form.cleaned_data['gender']
#
#             # Getting Profile Pic first
#             # First Check whether the file is selected or not
#             # Upload only if file is selected
#             if len(request.FILES) != 0:
#                 profile_pic = request.FILES['profile_pic']
#                 fs = FileSystemStorage()
#                 filename = fs.save(profile_pic.name, profile_pic)
#                 profile_pic_url = fs.url(filename)
#             else:
#                 profile_pic_url = None
#
#
#             try:
#                 user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
#                 user.students.address = address
#
#                 course_obj = Courses.objects.get(id=course_id)
#                 user.students.course_id = course_obj
#
#                 session_year_obj = SessionYearModel.objects.get(id=session_year_id)
#                 user.students.session_year_id = session_year_obj
#
#                 user.students.gender = gender
#                 user.students.profile_pic = profile_pic_url
#                 user.save()
#                 messages.success(request, "Student Added Successfully!")
#                 return redirect('staff_add_student')
#             except:
#                 messages.error(request, "Failed to Add Student!")
#                 return redirect('staff_add_student')
#         else:
#             return redirect('staff_add_student')
#
#
# def staff_edit_student_save(request):
#     if request.method != "POST":
#         return HttpResponse("Invalid Method!")
#     else:
#         student_id = request.session.get('student_id')
#         if student_id == None:
#             return redirect('/staff_manage_student')
#
#         form = EditStudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             username = form.cleaned_data['username']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             address = form.cleaned_data['address']
#             course_id = form.cleaned_data['course_id']
#             gender = form.cleaned_data['gender']
#             session_year_id = form.cleaned_data['session_year_id']
#
#             # Getting Profile Pic first
#             # First Check whether the file is selected or not
#             # Upload only if file is selected
#             if len(request.FILES) != 0:
#                 profile_pic = request.FILES['profile_pic']
#                 fs = FileSystemStorage()
#                 filename = fs.save(profile_pic.name, profile_pic)
#                 profile_pic_url = fs.url(filename)
#             else:
#                 profile_pic_url = None
#
#             try:
#                 # First Update into Custom User Model
#                 user = CustomUser.objects.get(id=student_id)
#                 user.first_name = first_name
#                 user.last_name = last_name
#                 user.email = email
#                 user.username = username
#                 user.save()
#
#                 # Then Update Students Table
#                 student_model = Students.objects.get(admin=student_id)
#                 student_model.address = address
#
#                 course = Courses.objects.get(id=course_id)
#                 student_model.course_id = course
#
#                 session_year_obj = SessionYearModel.objects.get(id=session_year_id)
#                 student_model.session_year_id = session_year_obj
#
#                 student_model.gender = gender
#                 if profile_pic_url != None:
#                     student_model.profile_pic = profile_pic_url
#                 student_model.save()
#                 # Delete student_id SESSION after the data is updated
#                 del request.session['student_id']
#
#                 messages.success(request, "Student Updated Successfully!")
#                 return redirect('/staff_edit_student/'+student_id)
#             except:
#                 messages.success(request, "Failed to Uupdate Student.")
#                 return redirect('/staff_edit_student/'+student_id)
#         else:
#             return redirect('/staff_edit_student/'+student_id)
#
#
# def staff_delete_student(request, student_id):
#     student = Students.objects.get(admin=student_id)
#     try:
#         student.delete()
#         messages.success(request, "Student Deleted Successfully.")
#         return redirect('staff_manage_student')
#     except:
#         messages.error(request, "Failed to Delete Student.")
#         return redirect('staff_manage_student')


# 管理固件页面
def manage_hardware(request):
    # if not hasattr(request.user, 'adminuser'):
    #     return redirect('admin_home')

    # firmware_list = FirmwareUpload.objects.all()
    # 只获取当前用户上传的固件
    firmware_list = FirmwareUpload.objects.filter(uploaded_by=request.user).order_by('-upload_date')
    context = {"firmware_list": firmware_list}
    return render(request, 'staff_template/hardware/manage_hardware_template.html', context)

# 上传固件页面
def add_hardware(request):
    # if not hasattr(request.user, 'adminuser'):
    #     return redirect('admin_home')
    return render(request, 'staff_template/hardware/add_hardware_template.html')

# 保存上传的固件
def add_hardware_save(request):
    if request.method != "POST":
        messages.error(request, "无效的请求方法")
        return redirect('staff_add_hardware')

    try:
        # firmware_version = request.POST.get('firmware_version')
        description = request.POST.get('description', '')
        firmware_file = request.FILES.get('firmware_file')

        # 验证文件
        if not firmware_file:
            messages.error(request, "请选择要上传的固件文件")
            return redirect('staff_add_hardware')

        # 检查文件大小 (2MB = 2 * 1024 * 1024 bytes)
        max_size = 2 * 1024 * 1024
        if firmware_file.size > max_size:
            messages.error(request, "文件大小不能超过2MB")
            return redirect('staff_add_hardware')

        # 保存固件信息
        firmware = FirmwareUpload(
            # firmware_version=firmware_version,
            file_name=firmware_file.name,
            file_size=firmware_file.size,
            file=firmware_file,
            description=description,
            uploaded_by=request.user
        )
        firmware.save()

        messages.success(request, "固件上传成功！")
        return redirect('staff_manage_hardware')

    except Exception as e:
        messages.error(request, f"上传失败: {str(e)}")
        return redirect('staff_add_hardware')

# 下载固件文件
def download_firmware(request, firmware_id):
    try:
        firmware = FirmwareUpload.objects.get(id=firmware_id)
        if os.path.exists(firmware.file.path):
            with open(firmware.file.path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = f'attachment; filename="{firmware.file_name}"'
                return response
        else:
            messages.error(request, "文件不存在")
    except FirmwareUpload.DoesNotExist:
        messages.error(request, "固件信息不存在")

    return redirect('staff_manage_hardware')

# 删除固件
def delete_hardware(request, hardware_id):
    try:
        firmware = FirmwareUpload.objects.get(id=hardware_id)
        # 删除文件
        if os.path.exists(firmware.file.path):
            os.remove(firmware.file.path)
        # 删除数据库记录
        firmware.delete()
        messages.success(request, "固件删除成功！")
    except FirmwareUpload.DoesNotExist:
        messages.error(request, "固件不存在")
    except Exception as e:
        messages.error(request, f"删除失败: {str(e)}")

    return redirect('staff_manage_hardware')

# 管理可执行文件页面
def manage_executable(request):
    # if not hasattr(request.user, 'adminuser'):
    #     return redirect('admin_home')

    executable_list = ExecutableUpload.objects.filter(uploaded_by=request.user).order_by('-upload_date')
    context = {"executable_list": executable_list}
    return render(request, 'staff_template/executable/manage_executable_template.html', context)

# 上传可执行文件页面
# @login_required
def add_executable(request):
    # if not hasattr(request.user, 'adminuser'):
    #     return redirect('admin_home')
    return render(request, 'staff_template/executable/add_executable_template.html')

# 保存上传的可执行文件
# @login_required
def add_executable_save(request):
    if request.method != "POST":
        messages.error(request, "无效的请求方法")
        return redirect('staff_add_executable')

    try:
        description = request.POST.get('description', '')
        executable_file = request.FILES.get('executable_file')

        # 验证文件
        if not executable_file:
            messages.error(request, "请选择要上传的可执行文件")
            return redirect('staff_add_executable')

        # 检查文件大小 (2MB = 2 * 1024 * 1024 bytes)
        max_size = 2 * 1024 * 1024
        if executable_file.size > max_size:
            messages.error(request, "文件大小不能超过2MB")
            return redirect('staff_add_executable')

        # 保存可执行文件信息
        executable = ExecutableUpload(
            file_name=executable_file.name,
            file_size=executable_file.size,
            file=executable_file,
            description=description,
            uploaded_by=request.user
        )
        executable.save()

        messages.success(request, "可执行文件上传成功！")
        return redirect('staff_manage_executable')

    except Exception as e:
        messages.error(request, f"上传失败: {str(e)}")
        return redirect('staff_add_executable')

# 下载可执行文件
# @login_required
def download_executable(request, executable_id):
    try:
        executable = ExecutableUpload.objects.get(id=executable_id)
        if os.path.exists(executable.file.path):
            with open(executable.file.path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = f'attachment; filename="{executable.file_name}"'
                return response
        else:
            messages.error(request, "文件不存在")
    except ExecutableUpload.DoesNotExist:
        messages.error(request, "可执行文件信息不存在")

    return redirect('staff_manage_executable')

# 删除可执行文件
# @login_required
def delete_executable(request, executable_id):
    try:
        executable = ExecutableUpload.objects.get(id=executable_id)
        # 删除文件
        if os.path.exists(executable.file.path):
            os.remove(executable.file.path)
        # 删除数据库记录
        executable.delete()
        messages.success(request, "可执行文件删除成功！")
    except ExecutableUpload.DoesNotExist:
        messages.error(request, "可执行文件不存在")
    except Exception as e:
        messages.error(request, f"删除失败: {str(e)}")

    return redirect('staff_manage_executable')