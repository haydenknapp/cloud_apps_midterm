<!DOCTYPE html>
<html>
<head>
<title>Log In</title>
</head>

<body>
% if error:
	<p style="color:red;">Duplicate username or password is shorter than 7 characters.</p>
% end

<form action='/insertuser' method='POST'>
Username:<br>
<input type='text' name='username'><br>
Full Name:<br>
<input type='text' name='fullname'><br>
Password:<br>
<input type='password' name='password'><br>
<input type='submit' value="Create Account"><br>
<a href='/login'>Have an account? Log in here.</a>
</form>


</body>

</html>
