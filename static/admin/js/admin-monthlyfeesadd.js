function AdmissionDates(){
  var x =document.getElementsByName("AdmissionDate")[0].value.trim();
  if(x.length==0)
  {
    document.getElementsByName("AdmissionDate")[0].style.border="1px solid red";
    document.getElementById("ErrorAdmissionDate").innerHTML="";
    return false;
  }else {
      document.getElementById("ErrorAdmissionDate").innerHTML="<i class='fas fa-check'></i>";
      document.getElementById("ErrorAdmissionDate").style.color="green";
      document.getElementsByName("AdmissionDate")[0].style.border="1px solid green";
      return true;
  }
} 
function Specials(){
  var x =document.getElementsByName("Special")[0].value.trim();
  if(x.length==0)
  {
    document.getElementsByName("Special")[0].style.border="1px solid red";
    document.getElementById("ErrorSpecial").innerHTML="";
    return false;
  }else {
      document.getElementById("ErrorSpecial").innerHTML="<i class='fas fa-check'></i>";
      document.getElementById("ErrorSpecial").style.color="green";
      document.getElementsByName("Special")[0].style.border="1px solid green";
      return true;
  }
} 
function FeesTypes(){
  var x =document.getElementsByName("FeesType")[0].value.trim();
  if(x.length==0)
  {
    document.getElementsByName("FeesType")[0].style.border="1px solid red";
    document.getElementById("ErrorFeesType").innerHTML="";
    return false;
  }else {
      document.getElementById("ErrorFeesType").innerHTML="<i class='fas fa-check'></i>";
      document.getElementById("ErrorFeesType").style.color="green";
      document.getElementsByName("FeesType")[0].style.border="1px solid green";
      return true;
  }
} 

function Paids(){
var x =document.getElementsByName("Paid")[0].value.trim();
if(x.length==0)
{
document.getElementsByName("Paid")[0].style.border="1px solid red";
document.getElementById("ErrorPaid").innerHTML="";
return false;
}else {
  document.getElementById("ErrorPaid").innerHTML="<i class='fas fa-check'></i>";
  document.getElementById("ErrorPaid").style.color="green";
  document.getElementsByName("Paid")[0].style.border="1px solid green";
  return true;
}
}  
function checkID()
{
var x =document.getElementsByName("StudentId")[0].value.trim();
if(x.length==0)
{
  document.getElementsByName("StudentId")[0].style.border="1px solid red";
  document.getElementById("ErrorStudentId").innerHTML="";
  return false;
}
else
{
  if( /^([0-9])+\-([0-9])+\-([a-zA-Z' '])/.test(x) || /^([0-9])+\-([0-9])+\-([0-9])+$/.test(x) || /^([0-9])+\-([0-9])+\-([0-9])+[a-zA-Z' ']/.test(x))
  {
    document.getElementById("ErrorStudentId").innerHTML="<i class='fas fa-check'></i>";
    document.getElementById("ErrorStudentId").style.color="green";
    document.getElementsByName("StudentId")[0].style.border="1px solid green";
    return true;
  }
  else
  {
    document.getElementsByName("StudentId")[0].style.border="1px solid red";
    document.getElementById("ErrorStudentId").innerHTML="Invalid ID (ex : (19-0001-NA Or 19-0002-6 Or 19-0002-6=6B) Here 19 = admission year '-' 0001 = student id '-' NA = Nursery Sec A Or 6 = class 6 Or 6B=Class 6 sec B)";
    document.getElementById("ErrorStudentId").style.color="red";
    return false;
  }
}
    
}

function checkClass()
{

var x =document.getElementsByName("Class")[0].value.trim();
if(x.length==0)
{
  document.getElementsByName("Class")[0].style.border="1px solid red";
  document.getElementById("ErrorClass").innerHTML="";
  return false;
}
else if(x>12)
{
    document.getElementsByName("Class")[0].style.border="1px solid red";
    document.getElementById("ErrorClass").innerHTML="Invalid Class";
    document.getElementById("ErrorClass").style.color="red";
    return false;
}
else
{
  if(/^([0-9])+$/.test(x) || /^[a-zA-Z]/.test(x))
  {
    document.getElementById("ErrorClass").innerHTML="<i class='fas fa-check'></i>";
    document.getElementById("ErrorClass").style.color="green";
    document.getElementsByName("Class")[0].style.border="1px solid green";
    return true;
  }
        
  else
  {
          
    document.getElementsByName("class")[0].style.border="1px solid red";
    document.getElementById("ErrorClass").innerHTML="Invalid Class";
    document.getElementById("ErrorClass").style.color="red";
    return false;
  }
}
}

function checkSection()
{
var x =document.getElementsByName("Section")[0].value.trim();
if(x.length==0)
{
document.getElementsByName("Section")[0].style.border="1px solid red";
document.getElementById("ErrorSection").innerHTML="";
return false;
}
else
{
if(!/^[a-zA-Z' ']/.test(x))
{
  document.getElementsByName("Section")[0].style.border="1px solid red";
  document.getElementById("ErrorSection").innerHTML="Only Letter allowed";
  document.getElementById("ErrorSection").style.color="red";
  return false;
}
else
{
  document.getElementById("ErrorSection").innerHTML="<i class='fas fa-check'></i>";
  document.getElementById("ErrorSection").style.color="green";
  document.getElementsByName("Section")[0].style.border="1px solid green";
  return true;
}
}

}



function StudentNames()
{
 
var x =document.getElementsByName("StudentName")[0].value.trim();
if(x.length==0)
{
document.getElementsByName("StudentName")[0].style.border="1px solid red";
document.getElementById("ErrorStudentName").innerHTML="";
return false;
}
else
{
if(!/^[a-zA-Z' ']/.test(x) )
{
  document.getElementsByName("StudentName")[0].style.border="1px solid red";
  document.getElementById("ErrorStudentName").innerHTML="Only Letter allowed";
  document.getElementById("ErrorStudentName").style.color="red";
  return false;
}
else
{
  document.getElementById("ErrorStudentName").innerHTML="<i class='fas fa-check'></i>";
  document.getElementById("ErrorStudentName").style.color="green";
  document.getElementsByName("StudentName")[0].style.border="1px solid green";
  return true;
}
}

}




function check()
{
checkClass();
checkID();
checkSection();
StudentNames();
Paids();
FeesTypes();
Specials();
AdmissionDates();

if(FeesTypes()==true &&Specials()==true  &&Paids()==true && checkClass()==true && checkSection()==true && checkID()==true && checkSection()==true && StudentNames()==true && AdmissionDates()==true)
    {
     
         
      
            event.preventDefault();
            var StudentId = $("#StudentId").val()
            var AdmissionDate = $("#AdmissionDate").val()
            var StudentName = $("#StudentName").val()
           
            var Class = $("#Class").val()
            var Section = $("#Section").val()
            var FeesType = $("#FeesType").val() 
            var Special = $("#Special").val()
            var Paid = $("#Paid").val()

            
         
           
              $.ajax({
                    method:'POST',
                    url: "AddMonthlyFees",
                    enctype : "multipart/form-data",
                    data: {
                        StudentId:StudentId,
                        AdmissionDate:AdmissionDate,
                        StudentName:StudentName,
                        Class:Class,
                        Section:Section,
                        FeesType:FeesType,
                        Special:Special,
                        Paid:Paid,
                        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                    },
                    success:function(response){
                        $('#SaveRooms').html(response)
                    }
                });
                setTimeout(function(){
                  $('#SaveRooms').empty() 
                },3000)
      
                $("#StudentId").val('')
                $("#AdmissionDate").val('')
                $("#StudentName").val('')
                $("#Class").val('')
                $("#Section").val('')
                $("#FeesType").val('') 
                $("#Special").val('') 
                $("#Paid").val('')

          
            
        
        return true;
    }
else{
    $("#SaveRooms").html('Empty Data or Invalid Data are Not Allowed').css('color','red')
    return false;
}
}
