#criar estrutura de nossos formularios
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,FileField
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField('E-mail',validators=[DataRequired(),Email()])
    senha = PasswordField('Senha',validators=[DataRequired()])
    botao_confirmacao = SubmitField('Fazer Login')

    def validate_emai(self,email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:

            raise ValidationError("Conta inexistente")


class FormCriarConta(FlaskForm):
    email = StringField('E-mail',validators=[DataRequired(),Email()])
    username = StringField('Nome de usuário',validators=[DataRequired()])
    senha = PasswordField('Inserir senha',validators=[DataRequired(),Length(6,20)])
    confirmar_senha = PasswordField('Confirmar Senha',validators=[DataRequired(),EqualTo("senha")])
    botao_confirmacao = SubmitField('Criar Conta')

    def validate_emai(self,email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado.')


class FormFoto(FlaskForm):
    foto = FileField("Imagem",validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")