
spool test.log

select 'hello' as message from dual;

spool off
select 'hello' as message from dual;
select * from system_control;