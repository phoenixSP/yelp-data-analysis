(:
How does a restaurant in one metropolitan area compare to the same business in another area (assuming they are a chain)?
ex: businesses with garage have higher rating than those with no garage
:)
let  $business := /root/business

let $bus_with_same_name :=(
	for $x in $business
	where $x/name="KFC"
	return $x
)

let $bus_xml := (
	let $xml:=(
	for $x in $bus_with_same_name
	return
		<business city="{$x/city}" state="{$x/state}"> {data($x/stars)} </business>)
	return
		<BB>
		{$xml}
		</BB>
)

let $avg_rating := avg(data($bus_xml/business))
let $result :=(
	for $v in distinct-values($bus_xml/business/@state)
	return 
		<state name="{$v}"> {avg(data($bus_xml/business[@state=$v]))} </state>
	)

return $result

