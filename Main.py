from nicegui import ui

encendido = False

def cambiar_estado():
    global encendido

    encendido = not encendido

    if encendido:
        estado.text = "Estado Actual: ON"
        estado.style('color: green; font-size: 24px')
        boton.set_text('Apagar')
        boton.props('color=green')
    else:
        estado.text = "Estado Actual: OFF"
        estado.style('color: red; font-size: 24px')
        boton.set_text('Encender')
        boton.props('color=red')

with ui.column().classes('w-full h-screen items-center justify-center'):

    with ui.card().style(
        'width:300; background-color:blue; color:white;'
    ).classes('items-center'):

        ui.label('Mi primera app').style(
        'font-size: 24px; font-weight: bold;'
        )

        ui.image(
            'nice.png'
        ).style('width:250px')

        estado = ui.label(
        "Estado Actual: OFF"
        ).style(
        'color: red; font-size: 24px;'
        )

        boton = ui.button(
            'Encender',
            icon = 'lightbulb',
            color = 'Red',
            on_click = cambiar_estado,
        ).style('color: white')

ui.run()