<html>
<head>
<title>Posts</title>

<style>
table, th, td {
	border: 1px solid black;
	border-collapse: collapse;
}
th, td {
	padding: 15px;
}
</style>
</head>


<body>
<h1>Welcome, {{fullname}}</h1>
<p><a href='/logout'>Log Out</a></p>
<table>
% for post in posts:
	<tr>
		<td>{{post['author']}}</td>
		<td>{{post['contents']}}</td>
		<form action='/updatepost/{{post['_id']}}' method='POST'>
		<td><input type='text' size='10' name='newContents'></td>
		<td><input type='submit' value='Update Post'></td>
		</form>
	</tr>
% end
</table><br>
Add new post:<br>
<form action='/makepost' method='POST'>
	<input type='text' name='contents'>
	<input type='submit' value='New Post'><br>
</body>
</html>
