from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Coupon

def apply_coupon(request):
    user = request.user
    if request.method == "POST":
        coupon_code = request.POST.get("code")
        try:
            coupon = Coupon.objects.get(coupon_code=coupon_code, is_active=True, is_redeemed = False)
            request.session["coupon_id"] = str(coupon.id)
            request.session["coupon_discount"] = coupon.discount
            data = { 
            "status" : "Coupon Applied! Redeem coupon to get discount"
            }
            return JsonResponse(data)
        except:
            data = { 
            "status" : "Invalid Coupon or Coupon Redeemed"
            }
            return JsonResponse(data)
    else:
        return redirect("products:product_list")

def remove_coupon(request):
    try:
        del request.session['coupon_id']
        del request.session["coupon_discount"]
        data = { 
        "status" : "Coupon Removed"
        }
        return JsonResponse(data)
    except:
        pass