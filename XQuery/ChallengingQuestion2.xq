

let $all_business := /root/business


let $business_element := (
  for $business in $all_business where $business//is_open = 1
  return 
  <business> 
  <business_id type="str">{$business//business_id}</business_id>
  <name type="str">{$business//name}</name>
  <latitude type="float">{$business//latitude}</latitude>
  <longitude type="float">{$business//longitude}</longitude>
  <stars type="float">{$business//starts}</stars>
  <review_count type="int">{$business//review_count}</review_count>
  <categories type="str">{$business//categories}</categories>
  </business>
)
  
  return <root>{$business_element}</root>

  