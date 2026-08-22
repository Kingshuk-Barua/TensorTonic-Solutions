select a.username, coalesce(b.username, 'organic') as referrer_name
from user_referrals a left join user_referrals b
on a.referred_by = b.id
order by a.username asc