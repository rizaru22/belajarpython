import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

pendapatan=ctrl.Antecedent(np.arange(0,50,5),'pendapatan')
nilaiUN=ctrl.Antecedent(np.arange(0,11,1),'nilaiUN')
kelayakan=ctrl.Consequent(np.arange(0,101,5),'kelayakan')

pendapatan.automf(3)
nilaiUN.automf(3)

pendapatan['poor']=fuzz.trapmf(pendapatan.universe,[0,0,5,15])
pendapatan['average']=fuzz.trimf(pendapatan.universe,[10,20,30])
pendapatan['good']=fuzz.trapmf(pendapatan.universe,[25,35,50,50])
# pendapatan.view()


nilaiUN['poor']=fuzz.trapmf(nilaiUN.universe,[0,0,4,6])
nilaiUN['average']=fuzz.trimf(nilaiUN.universe,[5,6,8])
nilaiUN['good']=fuzz.trapmf(nilaiUN.universe,[7,9,10,10])
# nilaiUN.view()

kelayakan['low']=fuzz.trapmf(kelayakan.universe,[0,0,20,70])
kelayakan['high']=fuzz.trapmf(kelayakan.universe,[50,90,100,100])
# kelayakan.view()

rule1=ctrl.Rule(pendapatan['poor']&nilaiUN['good'],kelayakan['high'])
rule2=ctrl.Rule(pendapatan['average']&nilaiUN['good'],kelayakan['high'])
rule3=ctrl.Rule(pendapatan['good']&nilaiUN['good'],kelayakan['low'])
rule4=ctrl.Rule(pendapatan['poor']&nilaiUN['average'],kelayakan['high'])
rule5=ctrl.Rule(pendapatan['average']&nilaiUN['average'],kelayakan['low'])
rule6=ctrl.Rule(pendapatan['good']&nilaiUN['average'],kelayakan['low'])
rule7=ctrl.Rule(pendapatan['poor']&nilaiUN['poor'],kelayakan['low'])
rule8=ctrl.Rule(pendapatan['average']&nilaiUN['poor'],kelayakan['low'])
rule9=ctrl.Rule(pendapatan['good']&nilaiUN['poor'],kelayakan['low'])

kelayakan_ctrl=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9])
kelayakanA=ctrl.ControlSystemSimulation(kelayakan_ctrl)

kelayakanA.input['pendapatan']=14
kelayakanA.input['nilaiUN']=7


kelayakanA.compute()
print(kelayakanA.output['kelayakan'])
kelayakan.view(sim=kelayakanA)
a=str(input("Masukkan a:"))