let $ranges := /root/business/attributes
let $price_one_stars := fn:avg($ranges[RestaurantsPriceRange2 eq "1"]/../stars)
let $price_two_stars := fn:avg($ranges[RestaurantsPriceRange2 eq "2"]/../stars)
let $price_three_stars := fn:avg($ranges[RestaurantsPriceRange2 eq "3"]/../stars)
return
<ratings>
<one>{$price_one_stars}</one>
<two>{$price_two_stars}</two>
<three>{$price_three_stars}</three>
</ratings>