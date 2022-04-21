from xml.dom.minidom import Document
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def home(request):
    return render(request, 'index.html')

def revenue(request):
      if request.method == 'POST':
          input_semester_name = request.POST["Semester"]
          input_year = request.POST["Year"]
          sql_query= "select MAJOR_ID, sum(ENROLLED*CREDIT_HOUR) as total from SECTION,COURSE where COURSE.COURSE_ID=SECTION.COURSE_ID and SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" group by MAJOR_ID "
          sql_query_total = "select sum(total) from ("+sql_query+") as dadao"

          with connection.cursor() as cursor_2:
            cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
            row2 = cursor_2.fetchall()
          with connection.cursor() as cursor_3:
            cursor_3.execute("select distinct SM_YEAR from SECTION")
            row3 = cursor_3.fetchall()
          with connection.cursor() as cursor_4:
            cursor_4.execute(sql_query)
            row4 = cursor_4.fetchall()
            
          with connection.cursor() as cursor_5:
            cursor_5.execute(sql_query_total)
            row5 = cursor_5.fetchall()
            
     
          return render(request, 'revenue.html',{"data4":row5,"data2":row2,"data3":row3,"data":row4,"sem_name":input_semester_name,"year":input_year})
      with connection.cursor() as cursor_2:
        cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
        row2 = cursor_2.fetchall()
      with connection.cursor() as cursor_3:
        cursor_3.execute("select distinct SM_YEAR from SECTION")
        row3 = cursor_3.fetchall()
      return render(request, 'revenue.html',{"data2":row2,"data3":row3})

def resources(request):
      if request.method == 'POST':
          input_semester_name = request.POST["Semester"]
          input_year = request.POST["Year"]
          sql_query="select MAJOR_ID, sum(ENROLLED),avg(ENROLLED) ,avg(ROOM.CAPACITY), (avg(ROOM.CAPACITY)-avg(ENROLLED)) from SECTION inner join COURSE on COURSE.COURSE_ID=SECTION.COURSE_ID inner join ROOM on ROOM.ROOM_ID=SECTION.ROOM_ID and SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" group by MAJOR_ID"
         
          # sql_query_total = "select sum(total) from ("+sql_query+") as dadao"

          with connection.cursor() as cursor_2:
            cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
            row2 = cursor_2.fetchall()
          with connection.cursor() as cursor_3:
            cursor_3.execute("select distinct SM_YEAR from SECTION")
            row3 = cursor_3.fetchall()
          with connection.cursor() as cursor_4:
            cursor_4.execute(sql_query)
            row4 = cursor_4.fetchall()
            
          # with connection.cursor() as cursor_5:
          #   cursor_5.execute(sql_query_total)
          #   row5 = cursor_5.fetchall()
            
     
          return render(request, 'mychart.html',{"data2":row2,"data3":row3,"data":row4,"sem_name":input_semester_name,"year":input_year})
      with connection.cursor() as cursor_2:
        cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
        row2 = cursor_2.fetchall()
      with connection.cursor() as cursor_3:
        cursor_3.execute("select distinct SM_YEAR from SECTION")
        row3 = cursor_3.fetchall()
      return render(request, 'mychart.html',{"data2":row2,"data3":row3})

def enrollment(request):
    if request.method == 'POST':
      input_semester_name = request.POST["Semester"]
      input_year = request.POST["Year"]
      input_choice1 = request.POST["Option"]
      if(input_choice1 == "1-10"):
          sql_query = "select MAJOR_ID, count(ENROLLED) as summury from SECTION inner join COURSE on COURSE.COURSE_ID=SECTION.COURSE_ID where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 1 and 10 group by MAJOR_ID"
      if(input_choice1 == "11-20"):
          sql_query = "select MAJOR_ID, count(ENROLLED) as summury from SECTION inner join COURSE on COURSE.COURSE_ID=SECTION.COURSE_ID where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 11 and 20 group by MAJOR_ID"
      if(input_choice1 == "21-30"):
          sql_query = "select MAJOR_ID, count(ENROLLED) as summury from SECTION inner join COURSE on COURSE.COURSE_ID=SECTION.COURSE_ID where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 21 and 30 group by MAJOR_ID"
      if(input_choice1 == "31-35"):
          sql_query = "select MAJOR_ID, count(ENROLLED) as summury from SECTION inner join COURSE on COURSE.COURSE_ID=SECTION.COURSE_ID where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 31 and 35 group by MAJOR_ID"
      if(input_choice1 == "36-40"):
          sql_query = "select MAJOR_ID, count(ENROLLED) as summury from SECTION inner join COURSE on COURSE.COURSE_ID=SECTION.COURSE_ID where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 36 and 40 group by MAJOR_ID"
      if(input_choice1 == "41-50"):
          sql_query = "select MAJOR_ID, count(ENROLLED) as summury from SECTION inner join COURSE on COURSE.COURSE_ID=SECTION.COURSE_ID where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 41 and 50 group by MAJOR_ID"
      if(input_choice1 == "51-55"):
          sql_query = "select MAJOR_ID, count(ENROLLED) as summury from SECTION inner join COURSE on COURSE.COURSE_ID=SECTION.COURSE_ID where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 51 and 55 group by MAJOR_ID"
      if(input_choice1 == "56-60"):
          sql_query = "select MAJOR_ID, count(ENROLLED) as summury from SECTION inner join COURSE on COURSE.COURSE_ID=SECTION.COURSE_ID where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 56 and 60 group by MAJOR_ID"
      if(input_choice1 == "60+"):
          sql_query = "select MAJOR_ID, count(ENROLLED) as summury from SECTION inner join COURSE on COURSE.COURSE_ID=SECTION.COURSE_ID where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED > 60 group by MAJOR_ID"
      sql_query_total = "select sum(summury) from ("+sql_query+") as dadao"

      with connection.cursor() as cursor_1:
        cursor_1.execute(sql_query)
        row1 = cursor_1.fetchall()
        
      with connection.cursor() as cursor_4:
        cursor_4.execute(sql_query_total)
        row4 = cursor_4.fetchall()

      with connection.cursor() as cursor_2:
        cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
        row2 = cursor_2.fetchall()
      with connection.cursor() as cursor_3:
        cursor_3.execute("select distinct SM_YEAR from SECTION")
        row3 = cursor_3.fetchall()
      return render(request, 'enrollment.html',{"data":row1,"data2":row2,"data3":row3,"data4":row4,"sem_name":input_semester_name,"year":input_year,"for":input_choice1})
    
    with connection.cursor() as cursor_2:
        cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
        row2 = cursor_2.fetchall()
    with connection.cursor() as cursor_3:
        cursor_3.execute("select distinct SM_YEAR from SECTION")
        row3 = cursor_3.fetchall()
    return render(request, 'enrollment.html',{"data2":row2,"data3":row3})

def classroom_req(request):
    if request.method == 'POST':
      input_semester_name = request.POST["Semester"]
      input_year = request.POST["Year"]
      input_choice1 = request.POST["Option"]
      if(input_choice1 == "1-10"):
          sql_query = "select * from SECTION where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 1 and 10"
      
      if(input_choice1 == "11-20"):
          sql_query = "select * from SECTION where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 11 and 20"
      
      if(input_choice1 == "21-30"):
          sql_query = "select * from SECTION where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 21 and 30"
      
      if(input_choice1 == "31-35"):
          sql_query = "select * from SECTION where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 31 and 35"
      
      if(input_choice1 == "36-40"):
          sql_query = "select * from SECTION where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 36 and 40"
      
      if(input_choice1 == "41-50"):
          sql_query = "select * from SECTION where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 41 and 50"
      
      if(input_choice1 == "51-55"):
          sql_query = "select * from SECTION where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 51 and 55"
      
      if(input_choice1 == "56-65"):
          sql_query = "select * from SECTION where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" and ENROLLED BETWEEN 56 and 65"
      
      sql_query_total="SELECT COUNT(*) AS ""Sections"",ROUND((COUNT(*)/14.0),2) AS ""Slot_of_7"", ROUND((COUNT(*)/16.0),2) AS ""Slot_of_8"" from ("+sql_query+") as dadao"
     
        
      with connection.cursor() as cursor_4:
        cursor_4.execute(sql_query_total)
        row4 = cursor_4.fetchall()

      with connection.cursor() as cursor_2:
        cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
        row2 = cursor_2.fetchall()
      with connection.cursor() as cursor_3:
        cursor_3.execute("select distinct SM_YEAR from SECTION")
        row3 = cursor_3.fetchall()
      return render(request, 'classroom_req.html',{"data2":row2,"data3":row3,"data4":row4,"sem_name":input_semester_name,"year":input_year,"for":input_choice1})
    
    with connection.cursor() as cursor_2:
        cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
        row2 = cursor_2.fetchall()
    with connection.cursor() as cursor_3:
        cursor_3.execute("select distinct SM_YEAR from SECTION")
        row3 = cursor_3.fetchall()
    return render(request, 'classroom_req.html',{"data2":row2,"data3":row3})



def data_input(request):
    if request.method == 'POST':
      input_enrollment = request.POST["input"]
      input_semester_name = request.POST["Semester"]
      input_year = request.POST["Year"]
      sql_query = "select MAJOR_ID, count(ENROLLED) from COURSE inner join SECTION on COURSE.COURSE_ID=SECTION.COURSE_ID and SEMESTER_NAME= '"+str(input_semester_name) +" ' and SM_YEAR="+str(input_year) +" and ENROLLED between 1 and "+str(input_enrollment)+" and BLOCKED = 0 group by MAJOR_ID"
      with connection.cursor() as cursor_1:
        cursor_1.execute(sql_query)
        row1 = cursor_1.fetchall()
      with connection.cursor() as cursor_2:
        cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
        row2 = cursor_2.fetchall()
      with connection.cursor() as cursor_3:
        cursor_3.execute("select distinct SM_YEAR from SECTION")
        row3 = cursor_3.fetchall()
      return render(request, 'data_input.html',{"data1":row1,"data2":row2,"data3":row3,"sem_name":input_semester_name,"year":input_year})
    
    with connection.cursor() as cursor_2:
        cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
        row2 = cursor_2.fetchall()
    with connection.cursor() as cursor_3:
        cursor_3.execute("select distinct SM_YEAR from SECTION")
        row3 = cursor_3.fetchall()
    return render(request, 'data_input.html',{"data2":row2,"data3":row3})


def course_infos(request):
    if request.method == 'POST':
      input_semester_name = request.POST["Semester"]
      input_year = request.POST["Year"]
      sql_query = "select SECTION.COURSE_ID,COURSE_NAME,sum(ENROLLED) from SECTION inner join COURSE on COURSE.COURSE_ID=SECTION.COURSE_ID where SEMESTER_NAME='"+str(input_semester_name) +"' and SM_YEAR="+str(input_year)+" group by COURSE_ID" 
      with connection.cursor() as cursor_1:
        cursor_1.execute(sql_query)
        row1 = cursor_1.fetchall()
      with connection.cursor() as cursor_2:
        cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
        row2 = cursor_2.fetchall()
      with connection.cursor() as cursor_3:
        cursor_3.execute("select distinct SM_YEAR from SECTION")
        row3 = cursor_3.fetchall()
      return render(request, 'course_infos.html',{"data":row1,"data2":row2,"data3":row3,"sem_name":input_semester_name,"year":input_year})
    
    with connection.cursor() as cursor_2:
        cursor_2.execute("select distinct SEMESTER_NAME from SECTION")
        row2 = cursor_2.fetchall()
    with connection.cursor() as cursor_3:
        cursor_3.execute("select distinct SM_YEAR from SECTION")
        row3 = cursor_3.fetchall()
    return render(request, 'course_infos.html',{"data2":row2,"data3":row3})







