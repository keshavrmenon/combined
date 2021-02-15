from ROOT import TCanvas, TTree, TH1F, TFile

c=TCanvas()

f=TFile("higgsCombineTest.MultiDimFit.mH125.123456.root")
f1=TFile("test.root", "RECREATE")
t1 = f.Get("limit")

a=1

h1 = TH1F("h_centre","r", 25, 0.25-a, 2.85-a)
h2 = TH1F("h_plus","+rErr", 25, 0.25-a, 2.85-a)
h3 = TH1F("h_minus","-rErr", 25, 0.25-a, 2.85-a)


for entry in t1:
    if(entry.quantileExpected == -1):
        h1.Fill(entry.r-a)
    elif(entry.quantileExpected>0):
        h2.Fill(entry.r-a)
    else:
        h3.Fill(entry.r-a)

f1.Write()
