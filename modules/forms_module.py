"""
Module 3: Forms
Learn about form handling, validation, and Flask-WTF
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, TextAreaField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

forms_bp = Blueprint('forms', __name__)


# Custom validator example
def validate_username(form, field):
    forbidden_usernames = ['admin', 'root', 'system']
    if field.data.lower() in forbidden_usernames:
        raise ValidationError('This username is not allowed.')


# Flask-WTF Form Classes
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send Message')


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                          validators=[DataRequired(), Length(min=3, max=20), validate_username])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])
    country = SelectField('Country', 
                         choices=[('', 'Select Country'), ('us', 'United States'), 
                                 ('uk', 'United Kingdom'), ('ca', 'Canada'), ('in', 'India')])
    terms = BooleanField('I agree to the Terms and Conditions', 
                        validators=[DataRequired()])
    submit = SubmitField('Register')


@forms_bp.route('/')
def forms_home():
    """Forms module home"""
    return render_template('forms_module/index.html')


@forms_bp.route('/basic-form', methods=['GET', 'POST'])
def basic_form():
    """Basic HTML form without Flask-WTF"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Simple validation
        errors = []
        if not name:
            errors.append('Name is required')
        if not email:
            errors.append('Email is required')
        if not message:
            errors.append('Message is required')
        
        if errors:
            return render_template('forms_module/basic_form.html', 
                                 errors=errors, 
                                 name=name, 
                                 email=email, 
                                 message=message)
        
        return render_template('forms_module/form_success.html', 
                             name=name, 
                             email=email, 
                             message=message)
    
    return render_template('forms_module/basic_form.html')


@forms_bp.route('/wtf-form', methods=['GET', 'POST'])
def wtf_form():
    """Form using Flask-WTF"""
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        
        flash(f'Thank you {name}! Your message has been sent.', 'success')
        return redirect(url_for('forms.wtf_form'))
    
    return render_template('forms_module/wtf_form.html', form=form)


@forms_bp.route('/registration', methods=['GET', 'POST'])
def registration():
    """Registration form with advanced validation"""
    form = RegistrationForm()
    
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('forms.forms_home'))
    
    return render_template('forms_module/registration.html', form=form)


@forms_bp.route('/file-upload', methods=['GET', 'POST'])
def file_upload():
    """File upload example"""
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(request.url)
        
        if file:
            filename = file.filename
            # In production, save the file: file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(f'File "{filename}" uploaded successfully!', 'success')
            return redirect(url_for('forms.file_upload'))
    
    return render_template('forms_module/file_upload.html')
