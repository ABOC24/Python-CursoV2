import tkinter as tk
import tkinter.messagebox as mb


class Alertas(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Alertas')
        self.geometry('350x350')

        btn_informacion = tk.Button(self, text='Mostrar alerta informativa')
        btn_informacion['command'] = self.mostrar_alerta_informativa
        
        btn_advertencia = tk.Button(self, text='Mostrar alerta de advertencia')
        btn_advertencia['command'] = self.mostrar_alerta_advertencia
        
        btn_error = tk.Button(self, text='Mostrar alerta de error')
        btn_error['command'] = self.mostrar_alerta_error

        opciones_botones = {
            'padx': 40,
            'pady': 5,
            'expand': True,
            'fill': tk.BOTH
        }

        btn_informacion.pack(**opciones_botones)
        btn_advertencia.pack(**opciones_botones)
        btn_error.pack(**opciones_botones)
    
    def mostrar_alerta_informativa(self):
        pass

    def mostrar_alerta_advertencia(self):
        pass

    def mostrar_alerta_error(self):
        pass


