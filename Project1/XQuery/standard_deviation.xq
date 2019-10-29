
let  $data := data(/root/review/useful)

let $mean :=  avg($data)

let $s :=(
for $d in $data
let $tmp := ($d - $mean)*($d - $mean)
return $tmp
)
let $total :=  math:pow( (sum($s) div count($data) ),0.5)
let $top_percent := 10 * $total
let $result_id := /root/review[useful >= $top_percent]/review_id
return <useful>
<id>{$result_id}</id>
</useful>