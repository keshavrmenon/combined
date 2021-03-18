from ROOT import TFile, TTree, TH1F
from array import array

f=open("args.txt","r")
L=f.readlines()
f.close()
f1=TFile("graviton_bias.root","RECREATE")
tree=TTree("tree", "Tree with pulls for masses and CATs")
mass=array('i',[0])
cat=array('i',[0])
rinj=array('f',[0.])
bias=array('f',[0.])
error=array('f',[0.])
tree.Branch("mass", mass, "mass/I")
tree.Branch("cat", cat, "cat/I")
tree.Branch("rinj", rinj, "rinj/F")
tree.Branch("bias", bias, "bias/F")
tree.Branch("error", error, "error/F")
j=0
for lines in L:
    icat=lines.split()[0]
    m=lines.split()[1]
    mu_inj=lines.split()[2]
    treename="higgsCombineDoubleHTag_"+icat+"_13TeV.BulkGraviton"+m+"_18_01_2021.t0.mu_inj"+mu_inj+"_envelop.MultiDimFit.mH125.123456.root"
    _f0=TFile.Open(treename)
    _t0=_f0.Get("limit")
    mass[0]=int(m)
    rinj[0]=float(mu_inj)
    cat[0]=int(icat)
    h_pull=TH1F("h_pull","h_pull",100, -5, 5)
    badentries=0
    for i in range (0, 1500, 3):
        _t0.GetEntry(i)
        r0=_t0.r
        _t0.GetEntry(i+1)
        rN=_t0.r
        _t0.GetEntry(i+2)
        rP=_t0.r
        if(r0>rinj[0]):
            sigmar=abs(r0-rP)
        else:
            sigmar=abs(r0-rN)
        if (sigmar==0):
            badentries+=1
            continue
        pull=(r0-rinj[0])/(sigmar)
        h_pull.Fill(pull)
    results=h_pull.Fit("gaus", "S")
    bias[0]=results.Parameter(1)
    error[0]=results.ParError(1)
    print(mass[0], cat[0], badentries)
    tree.Fill()
    tree.Show(j)
    j+=1
f1.Write()
f1.Close()
