<h1 class="pop">New user account creation</h1>

<p>
Enter your name, and email address, and password, and we'll email you with a confirmation to create your account.
</p>

<p>
If you've already got an account but can't log in, you can <% h.link_to('recover your password', url=h.url(controller='account', action='forgotten_password')) %>.
</p>

<&| @zookeepr.lib.form:fill, defaults=defaults, errors=errors &>

<form method="post" action="<% h.url_for() %>" >

<table class="form" summary="login form">

<tr>
	<th class="labels"><span class="mandatory">*</span><label for="registration.firstname">Your first name:</label></th>
	<td class="entries" valign="top"><% h.text_field('registration.firstname', size=40) %></td>
</tr>

<tr>
	<th class="labels"><span class="mandatory">*</span><label for="registration.lastname">Your last name:</label></th>
	<td class="entries"><% h.text_field('registration.lastname', size=40) %></td>
</tr>

<tr>
	<th class="labels"><span class="mandatory">*</span><label for="registration.email_address">Email address:</label></th>
	<td class="entries"><% h.text_field('registration.email_address', size=40) %></td>
</tr>

<tr>
	<th class="labels"><span class="mandatory">*</span><label for="registration.password">Choose a password:</label></th>
	<td class="entries"><% h.password_field("registration.password", size=40) %></td>
</tr>

<tr>
	<th class="labels"><span class="mandatory">*</span><label for="registration.password_confirm">Confirm your password:</label></th>
	<td class="entries"><% h.password_field("registration.password_confirm", size=40) %></td>
</tr>

<tr>
	<th class="labels"><span class="mandatory">*</span><label for="registration.handle">Display name:</label></th>
	<td class="entries"><% h.text_field('registration.handle', size=40) %>
	<br /><br />
		<p class="note">Your display name will be used to identify you on the website.</span>
	</td>
</tr>

<tr>
	<td>&nbsp;</td>
	<td class="submit"><% h.submit("Create a new account") %></td>
</tr>

</table>

</form>
</&>

<%args>
defaults
errors
</%args>