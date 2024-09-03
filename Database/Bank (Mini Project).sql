Select [AccountId],[CoustumerId],[FirstName],[LastName]
from [dbo].[AccountOwner] inner join [dbo].[Customer-Test]
on [dbo].[AccountOwner].[CoustumerId] = [dbo].[Customer-Test].[CustomerId]

select * from [dbo].[AccountOwner] inner join [dbo].[Customer-Test]
on [dbo].[AccountOwner].CoustumerId =  [dbo].[Customer-Test].CustomerId

Select * from [dbo].[AccountOwner] right outer join [dbo].[Customer-Test]
on [dbo].[AccountOwner].[CoustumerId] = [dbo].[Customer-Test].[CustomerId]

select * from [dbo].[AccountOwner] right outer join [dbo].[Customer-Test] 
on  [dbo].[AccountOwner].[CoustumerId] = [dbo].[Customer-Test].[CustomerId]




Select [AccountId],[CoustumerId],[FirstName],[LastName]
from [dbo].[AccountOwner]
inner join [dbo].[Customer-Test]
on [dbo].[AccountOwner].[CoustumerId] = [dbo].[Customer-Test].[CustomerId]


select * from [dbo].[AccountOwner] AO,[dbo].[Account-test] A
where AO.AccountId = A.AccountId


select * from [dbo].[Customer-Test]
where [CustomerId] not in (
	select [CoustumerId] from [dbo].[AccountOwner]

)


--delete from [dbo].[Account-test]
--where [Balance] like '%A%'

--delete from  [dbo].[Account-test]
--where [AccountId] not in (
--	select * from [dbo].[AccountOwner]
--)

update [dbo].[Customer-Test]
set [Blood] = 'o+' , [FirstName] = 'ali'
where [Blood] = 'o+' and [FirstName] = 'asdca'


update [dbo].[Account-test]
set [Balance] = [Balance] + [Balance] * 0.1
where [Balance] = 100


update [dbo].[Account-test]
set [Balance] = [Balance] + [Balance] * 0.1
where [Balance] = '110'


select count(*) as countCustomerTest
from [dbo].[Customer-Test]


select [Branch] , count(*) as countAccountTest
from [dbo].[Account-test]
group by [Branch]

select  [Branch] , count(*) as countAccountTest
from [dbo].[Account-test]
group by  [Branch]



select [AccountType] , count(*) as pp
from [dbo].[Account-test]
group by [AccountType] 

