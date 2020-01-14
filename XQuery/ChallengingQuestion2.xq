

let $all_business := /root/business


let $business_element := (
  for $business in $all_business where $business//is_open = 1
  return 
  <business> 
  {$business//business_id}
  {$business//name}
  {$business//latitude}
  {$business//longitude}
  {$business//starts}
  {$business//review_count}
  {$business//categories}
  </business>
)
  
  return <root>{$business_element}</root>

  
