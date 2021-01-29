from ROOT import TCanvas, TTree, TH1F, TFile

c=TCanvas()

f=TFile("higgsCombineTest.MultiDimFit.mH125.123456.root")
f1=TFile("test.root", "RECREATE")
t1 = f.Get("limit")

h1 = TH1F("h_centre","r", 25, -0.75+1, 1.85+1)
h2 = TH1F("h_plus","+rErr", 25, -0.75+1, 1.85+1)
h3 = TH1F("h_minus","-rErr", 25, -0.75+1, 1.85+1)


for entry in t1:
    if(entry.quantileExpected>0):
        h2.Fill(entry.r)
    elif(entry.quantileExpected == -1):
        h3.Fill(entry.r)
    else:
        h1.Fill(entry.r)

h1.Write()
h2.Write()
h3.Write()
