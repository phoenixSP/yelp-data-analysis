//gets total compliment counts for every user
for $user in /root/user
 let $cool := $user/compliment_cool
 let $cute := $user/compliment_cute
 let $funny := $user/compliment_funny
 let $hot := $user/compliment_hot
 let $list := $user/compliment_list
 let $more := $user/compliment_more
 let $note := $user/compliment_note
 let $photos := $user/compliment_photos
 let $plain := $user/compliment_plain
 let $profile := $user/compliment_profile
 let $writer := $user/compliment_writer
 return <total>{$cool + $cute + $funny + $hot + $list + $more +
                $note + $photos + $plain + $profile + $writer}</total>

//compliment aggregation statistics
let $totals := for $user in /root/user
 let $cool := $user/compliment_cool
 let $cute := $user/compliment_cute
 let $funny := $user/compliment_funny
 let $hot := $user/compliment_hot
 let $list := $user/compliment_list
 let $more := $user/compliment_more
 let $note := $user/compliment_note
 let $photos := $user/compliment_photos
 let $plain := $user/compliment_plain
 let $profile := $user/compliment_profile
 let $writer := $user/compliment_writer
 return <total>{$cool + $cute + $funny + $hot + $list + $more +
                $note + $photos + $plain + $profile + $writer}</total>
let $avg := fn:avg($totals)
let $min := fn:min($totals)
let $max := fn:max($totals)
return <stats><avg>{$avg}</avg><min>{$min}</min><max>{$max}</max><range>{$max - $min}</range></stats>


