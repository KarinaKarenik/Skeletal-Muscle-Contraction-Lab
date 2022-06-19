from PyQt5 import QtWidgets
import py.Menu, py.Theory1, py.Theory2, py.Theory3, py.Theory4, py.Experiment1_one, py.Experiment1_two, py.Experiment1_three, py.Experiment1_four, py.Experiment1_five
import py.Experiment2_one, py.Experiment2_two, py.Experiment2_three, py.Experiment2_four, py.Experiment2_five
import py.Experiment3_one, py.Experiment3_two, py.Experiment3_three, py.Experiment3_four, py.Experiment3_five
import py.Experiment4_1_one, py.Experiment4_1_two, py.Experiment4_1_three, py.Experiment4_2_one, py.Experiment4_2_two, py.Experiment4_2_three, py.Experiment4_conclussions
import py.Conclussions


class DataWindows:
    windows = [py.Menu.Menu(), #0
    py.Theory1.Theory1(),      #1
    py.Theory2.Theory2(),      #2
    py.Theory3.Theory3(),      #3
    py.Theory4.Theory4(),      #4
    
    py.Experiment1_one.Experiment1_one(),  #5
    py.Experiment1_two.Experiment1_two(),  #6
    py.Experiment1_three.Experiment1_three(),  #7
    py.Experiment1_four.Experiment1_four(), #8
    py.Experiment1_five.Experiment1_five(), #9
    
    py.Experiment2_one.Experiment2_one(),   #10
    py.Experiment2_two.Experiment2_two(),   #11
    py.Experiment2_three.Experiment2_three(),  #12
    py.Experiment2_four.Experiment2_four(),    #13
    py.Experiment2_five.Experiment2_five(),    #14

    py.Experiment3_one.Experiment3_one(), #15
    py.Experiment3_two.Experiment3_two(), #16
    py.Experiment3_three.Experiment3_three(), #17
    py.Experiment3_four.Experiment3_four(), #18
    py.Experiment3_five.Experiment3_five(), #19


    py.Experiment4_1_one.Experiment4_1_one(), #20
    py.Experiment4_1_two.Experiment4_1_two(), #21
    py.Experiment4_1_three.Experiment4_1_three(), #22
    py.Experiment4_2_one.Experiment4_2_one(), #23
    py.Experiment4_2_two.Experiment4_2_two(), #24
    py.Experiment4_2_three.Experiment4_2_three(), #25
    py.Experiment4_conclussions.Experiment4_conclussions(), #26
    
    py.Conclussions.Conclussions() #27
    ]
    
    windows[6].loadChart(windows[7])
    windows[23].loadChart(windows[24])


    widgets = QtWidgets.QStackedWidget()
    widgets.setFixedWidth(1000)
    widgets.setFixedHeight(750)
    
    for win in windows:
        widgets.addWidget(win)
        
        
        
        
        