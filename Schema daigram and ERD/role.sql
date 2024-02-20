--Example

Create or replace role demo_role ;

Grant usage on warehouse compute_wh to demo_role;

CREATE user damon password = "user123" comment = "for testing purpose";

Grant role demo_role to user damon;

Grant usage on schema Testing.public to demo_role;

grant select on all tables in schema testing.public to role demo_role;


select * from roles_table;