from gooey import Gooey, GooeyParser

@Gooey(program_name = "2d Gradient Tool",
       default_size = (900, 600),
       navigation = 'TABBED',
       header_bg_color = '#DDD',
       body_bg_color= '#EEE')

def parse_args():
    parser = GooeyParser()
    colors = parser.add_argument_group('Choose Colors')

    colors.add_argument('top_left',
                        metavar = 'Top Left Color',
                        widget = 'ColourChooser')

    colors.add_argument('top_left',
                    metavar = 'Top Left Color',
                    widget = 'ColourChooser')

    colors.add_argument('top_left',
                metavar = 'Top Left Color',
                widget = 'ColourChooser')

    colors.add_argument('top_left',
            metavar = 'Top Left Color',
            widget = 'ColourChooser')
                        

    args = parser.parse_args()
    return args

if __name__=='__main__':
    args = parse_args()

    
    
