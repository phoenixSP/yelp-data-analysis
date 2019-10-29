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
	
	return
		<HourList>
		 {$hourList}
		 </HourList>
    	
};

let  $checkin := /root/checkin
let $result :=(
for $c in $checkin
	let $t:= local:GenerateHours($c)
	let $resultList :=(
		for $v in distinct-values(data($t/hour))
		return 
			<hour name="{$v}"> {count(index-of(data($t/hour), $v))}  </hour>
	)
return
	<business business_id ="{$c/business_id}"> 
	{$resultList}
	</business>
)

for $v in distinct-values($result/hour/@name)
order by $v
return 
	<data hour="{$v}"> {sum(data($result/hour[@name=$v]))}
	</data>
