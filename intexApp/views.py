from django.db.models import Avg
from django.shortcuts import render
from intexApp.models import PdPrescribersCredentials, PdDrugs, PdTriple, PdStatedata, PdPrescriber

# Create your views here.

def indexPageView(request) :
    return render(request, 'intexApp/index.html')

def drugPageView(request) :
    data = PdDrugs.objects.all()
    context = {
        "drug" : data,

    }
    return render(request, 'intexApp/layout-sidenav-light.html', context)

def singleDrugPageView(request, drugname) :
    data = PdDrugs.objects.get(drugname = drugname)
    ten = PdTriple.objects.filter(drugname=drugname).order_by('-qty')[:10]
    #presdata = PdPrescriber.objects.raw(f"select npi, fname, lname, { finaldrugname } from pd_prescriber order by { finaldrugname } desc limit 10")
    context = {
        "drug" : data,
        #"pres" : presdata,
        "drugs" : ten,
    }
    return render(request, 'intexApp/singleDrug.html', context)

def searchDrugsPageView(request):
    if request.method == "POST":
        #search = request.POST['search']
        search_DN = request.POST['searchDN']
        search_IS = request.POST.get('searchIS')
        results = (PdDrugs.objects.filter(isopioid__istartswith=search_IS, drugname__istartswith=search_DN))
        context = {
            "drug" : results
        }
        return render(request, 'intexApp/layout-sidenav-light.html', context)
    data = PdDrugs.objects.all()
    context = {
        "drug" : data
    }
    return render(request, 'intexApp/layout-sidenav-light.html', context)


def prescriberPageView(request) :
    #data = PdPrescriber.objects.raw(f"select * from pd_prescriber order by npi")
    data = PdPrescriber.objects.all()
    context = {
        "pres" : data,

    }
    
    return render(request, 'intexApp/layout-static.html', context)

def opiateprescriberPageView(request) :
    data = PdPrescriber.objects.raw(f"select * from pd_prescriber where npi in (1275854911,1568563625,1902802762,1093893612,1053363903,1528472669,1316107147,1306917372,1093989899,1043338395,1962429308,1891704698,1700822368,1982882882,1285832071,1922233881,1134181829,1982970174,1609188432,1801071014,1760485072,1801970264,1447285770,1619105608,1255569653,1538177910,1073790622,1053388280,1891923793,1679696108,1801899141,1366445942,1982660544,1386647295,1689889354,1184720468,1669419909,1427148881,1881613594,1154310662,1215170626,1669434205,1629090220,1306994223,1831486471,1093821019,1730469081,1003824731,1841242799,1679599377,1184677379,1467405076,1265453047,1841279585,1265514822,1255507117,1861401440,1134186935,1124017165,1831395896,1346341351,1326156621,1891819603,1609856475,1992771174,1245547983,1295741635,1831260207,1417148545,1033179817,1023246253,1932546603,1598874422,1942202858,1912163114,1538250162,1891708541,1033415732,1427018621,1104037464,1093763047,1902910847,1881799922,1114168499,1093794257,1013198035,1265414940,1205862125,1851304679,1205978053,1033188461,1326356684,1760465850,1710960927,1174515084,1932463460,1881668986,1538138789,1841473394,1992097315,1699776377,1285988154,1477864429,1861467664,1790921484,1548577315,1710935705,1689712671,1811155112,1770553075,1821070970,1891776647,1740231463,1467408583,1194152710,1588612477,1104901909,1639197098,1053365528,1902922875,1407962343,1275551764,1396701207,1518928290,1912954637,1427016211,1053314633,1427048396,1780643742,1023336526,1295791309,1699732917,1538137633,1740238310,1962483024,1194713537,1427090810,1073654315,1831328798,1427053958,1750519906,1023379203,1386872588,1144395948,1215965520,1659473221,1578655148,1518036326,1942455464,1952489676,1902973266,1902974892,1780743559,1770526477,1003984915,1164650107,1760492748,1154601318,1730257346,1366528689,1952494718,1619094208,1841263209,1821226887,1720260441,1992899173,1619059920,1558407411,1548360621,1285848689,1730365669,1134161409,1558506949,1205866175,1447490016)")
    context = {
        "pres" : data
    }

    return render(request, 'intexApp/layout-static.html', context)
    
def singlePrescriberPageView(request, npi) :
    data = PdPrescriber.objects.get(npi = npi)
    cred = PdPrescribersCredentials.objects.filter(npi = npi)
    drugdata = PdTriple.objects.filter(prescriberid = npi)
    
    avg = []
    for i in drugdata :
        a = PdTriple.objects.all()
        ab = a.filter(drugname = i.drugname)
        avg.append(ab.aggregate(Avg('qty')))
        print(avg)


    context = {
        "pres" : data,
        "drug" : drugdata,
        "avg" : avg,
        "cred" : cred,
    }
    return render(request, 'intexApp/singlePrescriber.html', context)

def addPrescriberPageView(request) :
    if request.method == "POST" : 
        prescriber = PdPrescriber()
        prescriber.npi = request.POST['npi']
        prescriber.fname = request.POST['fname']
        prescriber.lname = request.POST['lname']
        prescriber.gender = request.POST['gender']
        prescriber.state = request.POST['state']
        prescriber.credentials = request.POST['credentials']
        prescriber.specialty = request.POST['specialty']
        prescriber.isopioidprescriber = request.POST['isopioidprescriber']
        prescriber.totalprescriptions = request.POST['totalprescriptions']

        prescriber.save()
        return prescriberPageView(request)
    else :
        return render(request, 'intexApp/addPrescriber.html')

def deletePrescriberPageView(request, npifr) :
    data = PdPrescriber.objects.get(npi = npifr)

    data.delete()

    return prescriberPageView(request)

def updatePresPageView(request):
    if request.method == 'POST' :
        npi = request.POST['npi']

        id = request.POST['drugid']

        customer = PdPrescriber.objects.get(npi=npi)
        triple = PdTriple.objects.get(id = id)

        customer.fname = request.POST['fname']
        customer.lname = request.POST['lname']
        customer.gender = request.POST['gender']
        customer.state = request.POST['state']
        customer.specialty = request.POST['specialty']
        customer.isopioidprescriber = request.POST['isopioidprescriber']
        customer.totalprescriptions = str(int(request.POST['totalprescriptions']) + (int(request.POST.get(id)) - triple.qty))#+ (request.POST.get(id) - triple.qty))
        customer.credentials = request.POST['credentials']
        

        customer.save()
        triple.save()

    return prescriberPageView(request)


def searchPrescribersPageView(request):
    if request.method == "POST":
        search_npi = request.POST['searchNPI']
        search_fn = request.POST['searchFN']
        search_ln = request.POST['searchLN']
        search_gen = request.POST['searchGEN']
        search_st = request.POST['searchST']
        search_sp = request.POST['searchSP']
        search_cred = request.POST['searchCRED']
        results = PdPrescriber.objects.filter(npi__istartswith=search_npi, fname__istartswith=search_fn, lname__istartswith=search_ln,
        gender__istartswith=search_gen, state__istartswith=search_st, specialty__istartswith=search_sp, credentials__istartswith=search_cred)
        context = {
            "pres" : results,
        }
        return render(request, 'intexApp/layout-static.html', context)


