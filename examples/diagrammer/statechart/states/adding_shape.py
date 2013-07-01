from kivy_statecharts.system.state import State

from kivy.graphics import Color

from kivy.uix.label import Label

from state_graphics import StateTriangleVectorShape
from state_graphics import StateRectangleVectorShape
from state_graphics import StatePentagonVectorShape


class AddingShape(State):
    '''The AddingShape state is a transient state -- after adding the shape,
    there is an immediate transition back to the ShowingDrawingArea state.'''

    def __init__(self, **kwargs):
        super(AddingShape, self).__init__(**kwargs)

    def enter_state(self, context=None):

        touch = self.statechart.app.touch

        # TODO: Finish other shapes.

        mode = self.statechart.app.state_drawing_mode_adapter.mode

        if mode == 'state_triangle':
            shape_cls = StateTriangleVectorShape
        elif mode == 'state_rectangle':
            shape_cls = StateRectangleVectorShape
        elif mode == 'state_pentagon':
            shape_cls = StatePentagonVectorShape
        elif mode == 'state_ellipse':
            shape_cls = StateTriangleVectorShape
        else:
            shape_cls = StateTriangleVectorShape

        drawing_area = \
                self.statechart.app.screen_manager.current_screen.drawing_area

        with drawing_area.canvas.before:
            Color(1, 1, 0)
            d = 100.
            #RectangleImageShape(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d),
                    #x=touch.x, y=touch.y, width=100.0, height=100.0,
                    #line_color=[1.0, .3, .2, .5], fill_color=[.4, .4, .4, .4])
            #Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            shape = shape_cls(
                    #pos=(touch.x - d / 2, touch.y - d / 2),
                    pos=(touch.x, touch.y),
                    size=(d, d),
                    #x=touch.x, y=touch.y, width=100.0, height=100.0,
                    stroke_width=5.0,
                    stroke_color=[.2, .9, .2, .8], fill_color=[.4, .4, .4, .4])

            label = Label(text="Some State", pos=shape.pos)
            shape.add_widget(label)

            #shape.add_widget(AnchoredLabel(
            #        anchor_widget=shape,
            #        text="Some State",
            #        label_anchor_x='left',
            #        label_anchor_y='bottom'))

            shape.generate_connection_points(10)

            self.statechart.app.shapes.append(shape)

            self.statechart.app.points.append(touch.pos)

            self.statechart.app.current_shape = shape

            self.go_to_state('ShowingDrawingArea')

    def exit_state(self, context=None):
        pass
