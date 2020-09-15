desc user;

-- 조회
select * from user;

-- 회원가입
insert into user values(null, '둘리', 'dooly@gmail.com', password('1234'),'male',now());

-- login
select no, name from user where email='dooly@gmail.com' and password=password('1234');

-- 회원정보 수정
select name, email, gender from user where no = 2;

update user set name='', gender ='' where no = 2;
update user set name='', gender ='', password = password('') where no = 2;