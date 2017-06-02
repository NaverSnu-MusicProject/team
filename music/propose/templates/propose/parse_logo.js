<!DOCTYPE html>
<html>
<head>
<title>reading file</title>
<script type="text/javascript">

var reader = new FileReader();

function readText(that){

	if(that.files && that.files[0]){
		var reader = new FileReader();
		reader.onload = function (e) {  
			var output=e.target.result;

			//process text to show only lines with "@":				
			output=output.split("\n").filter(/./.test, /\@/).join("\n");

			document.getElementById('main').innerHTML= output;
		};//end onload()
		reader.readAsText(that.files[0]);
	}//end if html5 filelist support
} 
</script>
</head>
<body>
<input type="file" onchange='readText(this)' />
<div id="main"></div>
</body>
</html>

