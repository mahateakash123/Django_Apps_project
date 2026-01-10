from django.shortcuts import render
from django.http import HttpResponse

def employee(request):
    str1 = """
    <html>
    <body bgcolor="skyblue">
    <center>
    <h1> EMPLOYEE DETAILS </H1>
    <table border=10>
    <tr>
        <th> EMPID </th>
        <th> EMPNAME </th>
        <th> SALARY </th>
    </tr>
    <tr>
        <td> 101 </td>
        <td> AKash </td>
        <td> 20000 </td>
    </tr>
    <tr>
        <td> 102 </td>
        <td> vishal </td>
        <td> 30000 </td>
    </tr>
    <tr>
        <td> 103 </td>
        <td> datta </td>
        <td> 27000 </td>
    </tr>
    </table>
    </center>
    </body>
    </html>
    """
    return HttpResponse(str1)

def customer(request):

    str2 = """
    <html>
    <body bgcolor="blue">
    <center>
    <h1> Customer Details </H1>
    <table border=10>
    <tr>
        <th> CUSTID </th>
        <th> CUSTNAME </th>
        <th> BALANCE </th>
    </tr>
    <tr>
        <td> 101 </td>
        <td> AKash </td>
        <td> 20000 </td>
    </tr>
    <tr>
        <td> 102 </td>
        <td> vishal </td>
        <td> 30000 </td>
    </tr>
    <tr>
        <td> 103 </td>
        <td> datta </td>
        <td> 27000 </td>
    </tr>
    </table>
    </center>
    </body>
    </html>
    """
    return HttpResponse(str2)
    

def student(request):
    str3 = """
    <html>
    <body bgcolor="red">
    <center>
    <h1> STUDENT DETAILS </H1>
    <table border=10>
    <tr>
        <th> STDID </th>
        <th> STDNAME </th>
        <th> FEE </th>
    </tr>
    <tr>
        <td> 101 </td>
        <td> AKash </td>
        <td> 20000 </td>
    </tr>
    <tr>
        <td> 102 </td>
        <td> vishal </td>
        <td> 30000 </td>
    </tr>
    <tr>
        <td> 103 </td>
        <td> datta </td>
        <td> 27000 </td>
    </tr>
    </table>
    </center>
    </body>
    </html>
    """
    return HttpResponse(str3)

