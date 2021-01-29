from ROOT import TCanvas, TTree, TH1F, TFile

c=TCanvas()

f=TFile("higgsCombineTest.MultiDimFit.mH125.123456.root")
f1=TFile("test.root", "RECREATE")
t1 = f.Get("limit")

h1 = TH1F("h_centre","", 100, -0.75, 1.85)
h2 = TH1F("h_plus","", 100, -0.75, 1.85)
h3 = TH1F("h_minus","", 100, -0.75, 1.85)


for entry in t1:
    if(entry.quantileExpected>0):
        h2.Fill(entry.r-1)
    elif(entry.quantileExpected == -1):
        h3.Fill(entry.r-1)
    else:
        h1.Fill(entry.r-1)

h1.Write()
h2.Write()
h3.Write()
