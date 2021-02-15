{
  gStyle->SetOptFit();
  TFile *_file0 = TFile::Open("higgsCombineDoubleHTag_0_13TeV.Radion300_18_01_2021.t0.mu_inj0.75_envelop.MultiDimFit.mH125.123456.root");
  TTree *_t0 =  (TTree*)_file0->Get("limit");
  float r0,rN,rP,qE,r, rinj=0.75, sigmar=0;
  _t0->SetBranchAddress("quantileExpected",&qE);
  _t0->SetBranchAddress("r",&r);
  TH1F *h_pull = new TH1F("h_pull","h_pull",100,-5,5);
  float pull;
  for (int i = 0; i< 1500; i=i+3)
    {
      //std::cout << i << std::endl;
      _t0->GetEntry(i);	
      r0 = r;
      _t0->GetEntry(i+1);
      rN = r;
      _t0->GetEntry(i+2);
      rP = r;
      if (r0 > rinj)
	sigmar=abs(r0-rP);
      else 
	sigmar=abs(r0-rN);
      pull=(r0-rinj)/(sigmar);
      h_pull->Fill(pull);
    }
  h_pull->Fit("gaus");
  h_pull->Draw();
}
