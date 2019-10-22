(:
let  $data := data(/root/user/useful)
:)
let $data := ( 4, 9, 11, 12, 17, 5, 8, 12, 14)
let $mean :=  avg($data)

let $s :=(
		for $d in $data
			let $tmp := ($d - $mean)*($d - $mean)
		return $tmp
	)
let $total :=  math:pow( (sum($s) div count($data) ),0.5)

return $total
