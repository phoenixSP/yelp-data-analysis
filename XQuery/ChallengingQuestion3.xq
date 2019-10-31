let $reviews := /root/review

let $words := ("HORRIBLE", "GREAT")

let $result := (
	for $w in $words
		let $reviews_filtered :=(
			for $x in $reviews
			where contains(upper-case($x/text), $w)
			return $x)
	return 
		<stat word="{$w}"> {avg($reviews_filtered/stars)} </stat>
)

return $result
