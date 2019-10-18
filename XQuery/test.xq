let  $checkin := /root/checkin
let $dtimeStringList := $checkin/date
let $dtimeString := data($dtimeStringList[2])

let $map := map{}
for $dateTime in tokenize($dtimeString, ",")
	let $hour := substring-before($dateTime, ':')
	let $hour := substring($hour, string-length($hour)-1)
	return $hour
