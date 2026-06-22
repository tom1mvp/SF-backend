from django.core.mail import send_mail
from django.conf import settings

class EmailServices:
    @staticmethod
    def send_welcome_email(to_email, username):
        subject='¡Bienvenido a SF-5!'
        message = f"Hola {username},\n\n¡Tu cuenta fue creada con éxito! Ya podés ingresar y reservar tus canchas favoritas."
        
        html_message = f"""
        <div style="font-family: sans-serif; padding: 20px; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px;">
            <h2 style="color: #28a745; text-align: center;">¡Tu cuenta está lista, {username}!</h2>
            <p style="font-size: 16px; color: #333;">Gracias por registrarte en nuestra plataforma.</p>
            <p style="font-size: 16px; color: #333;">Ya podés armar tus partidos, reservar canchas en tiempo real y gestionar tus torneos de la forma más rápida.</p>
            <div style="text-align: center; margin: 30px 0;">
                <a href="http://localhost:3000/login" style="background-color: #28a745; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">
                    Ir a Reservar Cancha
                </a>
            </div>
            <hr style="border: none; border-top: 1px solid #eee;" />
            <p style="font-size: 12px; color: #777; text-align: center;">SF-5 - Sistema de Gestión de Complejos Deportivos</p>
        </div>
        """
        
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[to_email],
                html_message=html_message,
                fail_silently=False
            )
            return True
        except Exception as e:
            print(f"Error enviando mail de bienvenida: {str(e)}")
            return False
    
    @staticmethod
    def send_reactivation_link_email(to_email, username, token): # Views (email)
        subject = 'Enlace de Reactivación de Cuenta - SF-5'
        
        reactivation_link = f"http://localhost:3000/confirm-reactivation?token={token}"
        
        message = f"Hola {username},\n\nPara reactivar tu cuenta de SF-5 y volver a realizar reservas, ingresá al siguiente enlace:\n{reactivation_link}"
        
        html_message = f"""
        <div style="font-family: sans-serif; padding: 20px; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px;">
            <h2 style="color: #0056b3; text-align: center;">Reactivá tu cuenta de SF-5</h2>
            <p style="font-size: 16px; color: #333; line-height: 1.5;">Hola <strong>{username}</strong>,</p>
            <p style="font-size: 16px; color: #555;">Recibimos una solicitud para reactivar tu cuenta en nuestra plataforma de gestión de turnos.</p>
            <p style="font-size: 16px; color: #555;">Para completar el proceso y volver a habilitar tu usuario, hacé click en el siguiente botón:</p>
            
            <div style="text-align: center; margin: 30px 0;">
                <a href="{reactivation_link}" style="background-color: #0056b3; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">
                    Reactivar Mi Cuenta
                </a>
            </div>
            
            <p style="font-size: 13px; color: #777;">Si el botón no funciona, podés copiar y pegar este enlace en tu navegador:<br>
            <a href="{reactivation_link}" style="color: #0056b3;">{reactivation_link}</a></p>
            
            <hr style="border: none; border-top: 1px solid #eee; margin-top: 30px;" />
            <p style="font-size: 12px; color: #999; text-align: center;">Si vos no solicitaste esto, podés ignorar este correo de forma segura.</p>
        </div>
        """
        
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[to_email],
                html_message=html_message,
                fail_silently=False
            )
            return True
        except Exception as e:
            print(f"Error enviando enlace de reactivación: {str(e)}")
            return False
        
    @staticmethod
    def send_account_reactivated_confirmation(to_email, username):
        subject = '¡Tu cuenta de SF-5 ya está activa!'
        
        link = "http://localhost:3000/login"
        message = f"Hola {username},\n\n¡Buenas noticias! Tu cuenta ha sido reactivada con éxito. Ya podés volver a ingresar a la plataforma:\n{link}"
        
        html_message = f"""
        <div style="font-family: sans-serif; padding: 20px; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px;">
            <h2 style="color: #28a745; text-align: center;">¡Bienvenido de vuelta, {username}!</h2>
            <p style="font-size: 16px; color: #333; line-height: 1.5;">Te avisamos que el proceso de reactivación se completó con éxito.</p>
            <p style="font-size: 16px; color: #333;">Tu usuario ya se encuentra completamente habilitado para volver a realizar reservas de canchas, armar partidos y prenderte en los torneos.</p>
            
            <div style="text-align: center; margin: 30px 0;">
                <a href="{link}" style="background-color: #28a745; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">
                    Iniciar Sesión Ahora
                </a>
            </div>
            
            <hr style="border: none; border-top: 1px solid #eee; margin-top: 30px;" />
            <p style="font-size: 12px; color: #777; text-align: center;">SF-5 - Sistema de Gestión de Complejos Deportivos</p>
        </div>
        """
        
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[to_email],
                html_message=html_message,
                fail_silently=False
            )
            return True
        except Exception as e:
            print(f"Error enviando confirmación de reactivación: {str(e)}")
            return False
    
    @staticmethod
    def send_password_reset_email(to_email, username, token): # Views (emails)
        subject = 'Restablecer Contraseña - SF-5'
        
        reset_link = f"http://localhost:3000/reset-password?token={token}"
        
        message = f"Hola {username},\n\nRecibimos una solicitud para restablecer tu contraseña. Ingresá al siguiente enlace para continuar:\n{reset_link}"
        
        html_message = f"""
        <div style="font-family: sans-serif; padding: 20px; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px;">
            <h2 style="color: #333; text-align: center;">¿Olvidaste tu contraseña?</h2>
            <p style="font-size: 16px; color: #555; line-height: 1.5;">Hola <strong>{username}</strong>,</p>
            <p style="font-size: 16px; color: #555;">Recibimos una solicitud para restablecer la contraseña de tu cuenta de SF-5.</p>
            <p style="font-size: 16px; color: #555;">Para elegir una nueva clave y proteger tu cuenta, hacé click en el botón de abajo:</p>
            
            <div style="text-align: center; margin: 30px 0;">
                <a href="{reset_link}" style="background-color: #dc3545; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">
                    Restablecer Contraseña
                </a>
            </div>
            
            <p style="font-size: 13px; color: #777; text-align: center;">Este enlace es de un solo uso y expirará pronto.</p>
            <p style="font-size: 13px; color: #999;">Si vos no solicitaste este cambio, podés ignorar este correo de forma segura; tu contraseña actual seguirá funcionando perfectamente.</p>
            
            <hr style="border: none; border-top: 1px solid #eee; margin-top: 30px;" />
            <p style="font-size: 12px; color: #777; text-align: center;">SF-5 - Sistema de Gestión de Complejos Deportivos</p>
        </div>
        """
        
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[to_email],
                html_message=html_message,
                fail_silently=False
            )
            return True
        except Exception as e:
            print(f"Error enviando mail de recuperación: {str(e)}")
            return False