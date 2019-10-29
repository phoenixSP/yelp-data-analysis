declare function local:GenerateHours($requestBody as element())
as element()* {
	let $dtimeStringList := $requestBody/date
	let $dtimeString := data($dtimeStringList)

	let $hourList :=(
		for $dateTime in tokenize($dtimeString, ",")
			let $hour := substring-before($dateTime, ':')
			let $hour := substring($hour, string-length($hour)-1)
	
		return 
		<hour> {$hour} </hour>
	)
	
	return (
    	<HourList>
           {$hourList}
       </HourList>
    	)
};

let  $checkin := /root/checkin
let $t:= local:GenerateHours($checkin[7])



let $resultList :=(
	for $v in distinct-values(data($t/hour))
	return 
		<element>
		<hour> {$v} </hour>
		<count> {count(index-of(data($t/hour), $v))} </count>
		</element>
		
	)

return $resultList
