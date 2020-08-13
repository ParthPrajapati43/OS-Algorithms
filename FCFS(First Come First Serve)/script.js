var last=0;
var table = new Array(100,6);
function AddRow(){
	var r1=document.getElementById("Input").insertRow(++last);
	for(var i=0;i<6;++i)
	{
		if(i<3)
		{
			var temp=r1.insertCell(i);
			temp.innerHTML = "\<input type=\"number\" id="+last+i+" size=\"4\"\>";
		}
		else
		{
			var temp=r1.insertCell(i);
			temp.innerHTML = "\<input type=\"number\" id="+last+i+" size=\"4\" disabled\>";
		}
	}
}
var start = new Array(last);
var Bus = new Array(last);
function solve(){
	for(var i=0;i<last;++i)
	{
		var a=i+1;
		var temp=document.getElementById(a+"1");
		var temp1=document.getElementById(a+"2");
		start[i]=temp.value;
		Bus[i]=temp1.value;
	}
}
console.log(Bus);
