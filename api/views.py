from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product, Customer, Sale

@csrf_exempt
def manage_products(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Validation
            if float(data['price']) <= 0:
                return JsonResponse({"status": "error", "message": "Price must be greater than 0"}, status=400)
            
            product = Product.objects.create(
                name=data['name'],
                description=data.get('description', ''),
                price=data['price'],
                stock=data.get('stock', 0)
            )
            return JsonResponse({"status": "success", "message": "Product added successfully", "id": product.id})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

@csrf_exempt
def get_customer_debt(request, customer_id):
    if request.method == 'GET':
        try:
            customer = Customer.objects.get(id=customer_id)
            return JsonResponse({
                "status": "success", 
                "customer": customer.name, 
                "utang_balance": float(customer.utang_balance)
            })
        except Customer.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Customer not found"}, status=404)
