#include <map>
#include <string>
#include <sstream>

#ifndef TBCALIB_h
#define TBCALIB_h

class TBCalibSource
{
private:
    std::map<std::string, double> qie8MIPCal_, qie11MIPCal_;

public:
    //MIP signal in fC for a 17 layer tower
    static constexpr double  QIE8MIP = 0.526322667;
    static constexpr double QIE11MIP = 174.4423444;

    double getQIE8Corr(int ieta, int iphi)
    {
	std::stringstream ss;
	ss << ieta << "_" << iphi;
	auto ref = qie8MIPCal_.find(ss.str());
	if(ref != qie8MIPCal_.end())  return ref->second;
	else                          return 1.0;
    }

    double getQIE11Corr(int ieta, int iphi, int depth)
    {
	std::stringstream ss;
	ss << ieta << "_" << iphi << "_" << depth;
	auto ref = qie11MIPCal_.find(ss.str());
	if(ref != qie8MIPCal_.end())  return ref->second;
	else                          return 1.0;
    }

    TBCalibSource()
    {
      //HPD 2017
      qie8MIPCal_["20_4"] = 0.9519207002;
      qie8MIPCal_["19_4"] = 0.9090138698;
      qie8MIPCal_["18_4"] = 0.8937375969;
      qie8MIPCal_["18_3"] = 1.2084573832;
      qie8MIPCal_["19_3"] = 1.0815190068;
      qie8MIPCal_["20_3"] = 1.0221021942;

      //SiPM 2017
      qie11MIPCal_["18_5_2"] = 1.134717199051;
      qie11MIPCal_["18_6_2"] = 1.057437817530; 
      qie11MIPCal_["19_5_2"] = 0.983309282677; 
      qie11MIPCal_["19_6_2"] = 0.966664511656; 
      qie11MIPCal_["20_5_2"] = 1.076470136508; 
      qie11MIPCal_["20_6_2"] = 1.017393820392; 
      qie11MIPCal_["18_5_3"] = 1.061592800556; 
      qie11MIPCal_["18_6_3"] = 1.069800265205; 
      qie11MIPCal_["19_5_3"] = 1.130889502122; 
      qie11MIPCal_["19_6_3"] = 1.175682915249; 
      qie11MIPCal_["20_5_3"] = 1.140630623758; 
      qie11MIPCal_["20_6_3"] = 1.252194237604; 
      qie11MIPCal_["18_5_4"] = 0.832268388052; 
      qie11MIPCal_["18_6_4"] = 0.996574219013; 
      qie11MIPCal_["19_5_4"] = 1.006471690880; 
      qie11MIPCal_["19_6_4"] = 0.945539918827; 
      qie11MIPCal_["20_5_4"] = 1.042500743704; 
      qie11MIPCal_["20_6_4"] = 1.080238687460; 
      qie11MIPCal_["18_5_5"] = 0.806307195698; 
      qie11MIPCal_["18_6_5"] = 0.825486112672; 
      qie11MIPCal_["19_5_5"] = 0.855896200893; 
      qie11MIPCal_["19_6_5"] = 0.899331050036; 
      qie11MIPCal_["20_5_5"] = 0.842350400524; 
      qie11MIPCal_["20_6_5"] = 0.900226779603; 
      qie11MIPCal_["18_5_6"] = 1.120608633430; 
      qie11MIPCal_["18_6_6"] = 1.268939226778; 
      qie11MIPCal_["19_5_6"] = 0.827522736066; 
      qie11MIPCal_["19_6_6"] = 0.982727634070; 
      qie11MIPCal_["20_5_6"] = 1.094560803933; 
      qie11MIPCal_["20_6_6"] = 1.073200760683;
    }
};

#endif
