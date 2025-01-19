// Check if the query parameter 'email_sent' is present
const params = new URLSearchParams(window.location.search);
if (params.has('email_sent')) {
    const status = params.get('email_sent');
    if (status === 'success') {
        Swal.fire({
            icon: 'success',
            title: 'Email Sent!',
            text: 'Your results have been sent successfully.',
        });
    } else if (status === 'error') {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'There was an issue sending the email. Please try again.',
        });
    }
}