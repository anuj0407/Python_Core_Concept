# Creating a E-commerce with a class that have a method name calculate_total(items,tax_rate)

class Ecom:
    # items : list of prices
    def calculate_total(self,items,tax_rate):
        total_bill = 0
        if tax_rate < 0 or tax_rate > 1:
            raise ValueError("Tax rate must be in range")
        
        for price in items:
            if price < 0:
                raise ValueError("Price can not be negative")
            else:
                total_bill += (price + price*(tax_rate/100))
        return round(total_bill,2)
