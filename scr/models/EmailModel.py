from scr.database.connectDB import get_connection
from scr.models.entities.Email import Email


# Listar Email
class EmailModel:
    @classmethod

    def listar_email(self):
        try:
            connection = get_connection()
            emails = []
            with connection.cursor() as cursor:
                sql = "SELECT  EMAIL, FECHAREGISTER FROM ExchangeRateEmail"
                cursor.execute(sql)
                datos = cursor.fetchall()
                for fila in datos:
                    email = Email(fila[0],fila[1])
                    emails.append(email.convert_to_JSON())
                connection.close()
                return emails
        except Exception as ex:
            raise Exception(ex)


    # Add Email
    @classmethod
    def add_email(self, email):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql_insert = "INSERT INTO ExchangeRateEmail (EMAIL, FECHAREGISTER) VALUES('{0}','{1}')".format(
                    email.email, email.fecharegister)

                cursor.execute(sql_insert)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    # Delete Email
    @classmethod
    def del_email(self, email):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql_del = "DELETE FROM ExchangeRateEmail WHERE EMAIL='{0}' ".format(
                    email.email)
                cursor.execute(sql_del)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
