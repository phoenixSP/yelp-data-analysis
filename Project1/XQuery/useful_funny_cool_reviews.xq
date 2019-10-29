declare function local:std_diff($num as xs:int, $avg as xs:double) as xs:double{
  let $diff := $num - $avg
  return <std_diff>math:pow($diff,2)</std_diff>
};
let $review := /root/review
let $cool_avg := xs:double(fn:avg($review/cool))
let $useful_avg := fn:avg($review/useful)
let $funny_avg := fn:avg($review/funny)
let $total_cool_differences := for $cool in $review/cool
return <total_diff>local:std_diff(xs:int($cool),$cool_avg)</total_diff>
return <reviews>
{$total_cool_differences}
</reviews>