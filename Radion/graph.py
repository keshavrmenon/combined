from ROOT import TFile, TTree, TGraph, TCanvas, TLatex, TH1F, TGraphErrors, TLegend

f=TFile.Open("radion_bias.root")
t=f.Get("tree")

c=TCanvas("c","c",900,900)
gr1= TGraphErrors()
gr2= TGraphErrors()
gr3= TGraphErrors()
colours=[632, 600, 419]
markers=[20,21,22]
list_graph=[]

gr1.SetTitle("CAT0")
gr1.GetXaxis().SetTitle("M_{X}[GeV]")
gr1.GetYaxis().SetTitle("Bias")
gr1.GetXaxis().SetLimits(250, 1010)
gr2.SetTitle("CAT1")
gr3.SetTitle("CAT2")

list_graph.append(gr1)
list_graph.append(gr2)
list_graph.append(gr3)

for i in range(3):
    list_graph[i].SetLineColor(colours[i])
    list_graph[i].SetMarkerColor(colours[i])
    list_graph[i].SetMarkerStyle(markers[i])
    list_graph[i].SetLineWidth(2)
    list_graph[i].SetMarkerSize(2)
    
for i in range(0,45,3):
    t.GetEntry(i)
    list_graph[0].SetPoint(int(i/3), t.mass, t.bias)
    list_graph[0].SetPointError(int(i/3), 0, t.error)
    t.GetEntry(i+1)
    list_graph[1].SetPoint(int(i/3), t.mass, t.bias)
    list_graph[1].SetPointError(int(i/3), 0, t.error)
    t.GetEntry(i+2)
    list_graph[2].SetPoint(int(i/3), t.mass, t.bias)
    list_graph[2].SetPointError(int(i/3), 0, t.error)

l=TLegend(0.7, 0.75, 0.9, 0.9)
l.SetFillStyle(-1)
l.SetBorderSize(0)
l.SetTextFont(42)
l.SetTextSize(0.03)

for i in range(3):
    if i==0 : list_graph[i].Draw("AP")
    else: list_graph[i].Draw("Psame")
    l.AddEntry(list_graph[i])
l.Draw()

#list_graph[0].GetYaxis.SetLimits(-0.3, 0.6)

c.SaveAs("radion_bias_plot.root")
