Class Request():
 	__tablename__ = "request"
    id=db.Column(db.Integer, primary_key=True)
    flag_used=db.Column(db.Boolean, default=False)
    method=db.Column(db.String)
    url=db.Column(db.String)


if __name__ = '__main__':
	req = Request
	data = [{
		flag_used: 0,
		method = "POST",
		url = "/test_1"
	},
	{
		flag_used: 0,
		method = "POST",
		url = "/test0"
	},
	{
		flag_used: 0,
		method = "GET",
		url = "/test1"
	},
	{
		flag_used: 1,
		method = "POST",
		url = "/test2"
	}]

	for d in data:
		req=Request(flag_used = d['flag_used'],
				method = d['method'],
				url = d['url'])
		db.session.add(req)
        db.session.flush()
        db.session.commit()










