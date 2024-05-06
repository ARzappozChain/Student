from .models import *


def getBaseData(request):
    
    # nabbar Text
    
    navbarText = Navbar_text.objects.all().last()
    
    # footer header text
    Footer_other_header_name = Footer_other_detail_header.objects.all()
    
    # footer li text
    
    CattegoryHeader = Footer_other_detail_header.objects.all()
    CattegoryHeaderData = {}
    
    for header in CattegoryHeader:
        CattegoryHeaderData[header] = Header_li.objects.filter(HeaderChoice = header )
        
        
    # payment merchent image
    
    Pyament_image = Payment_Merchant.objects.all()
    
    

    # fOOTER LAST PART
    
    footer_last = [Footer_Last_section.objects.last()]  # Wrap the object in a list
    
    
    return {'navbarText': navbarText, 
            'Footer_other_header_name':Footer_other_header_name, 
            'CattegoryHeaderData':CattegoryHeaderData,
            'Pyament_image': Pyament_image,
            'footer_last':footer_last,
            
            }
    