# Class For push button modularity
# Interrupt Handling - PB Switch Input
# Hardware Debounced button


#load libraries
import machine
import utime


class P_button:

    def __init__(self,PB_pin):
        self.PB_pin = PB_pin
        #self.Pb_Switch_State = 0
        self.Setup_Irqs()
        self.Pb_Switch_State_Old=0
        
    def Pb_Switch_INT(self,pin):         # PB_Switch Interrupt handler
       
        self.logic_sate = self.Pb_Switch.value()     # reference the global variable
        self.Pb_Switch.irq(handler=None) # Turn off the handler while it is executing
    
        #if (self.Pb_Switch_State_Old() == 1) and (self.Pb_Switch_State == 1):  # Pb_Switch is active (High) and Pb_Switch State is currently Low
        if (self.Pb_Switch.value() == 1): # Pb_Switch is active (High)
            self.Pb_Switch_State = 0    # Update current state of switch
            print("OFF")
        #elif (self.Pb_Switch_State_Old() == 0) and (self.Pb_Switch_State == 0): # Pb_Switch is not-active (Low) and Pb_Switch State is currently High
        elif (self.Pb_Switch.value() == 0): # Pb_Switch is not-active (Low)
              self.Pb_Switch_State = 1     # Update current state of switch
              print("ON")
    def Setup_Irqs(self):  

        #Creat an 'object' for our Pb_Switch change of state
        self.Pb_Switch = machine.Pin(self.PB_pin,machine.Pin.IN,machine.Pin.PULL_UP)
        self.Pb_Switch.irq(trigger=machine.Pin.IRQ_RISING, handler=self.Pb_Switch_INT)
         

