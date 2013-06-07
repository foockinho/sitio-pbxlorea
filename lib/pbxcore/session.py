from pbxcore.model import Model, WebSession, Account
import hashlib


def get_session(request):
    session_id = str(request.getSession().uid)
    return session_id


def update_address(model, account):
    if not account.btc_rx == account.get_address():
        account.btc_rx = account.get_address()
    model.session.commit()


def get_account(request, secret=False):
    model = Model()
    session_id = str(request.getSession().uid)
    web_session = model.query(WebSession).filter_by(session_id=session_id).first()

    # user input a secret... old session
    if secret or request.args.get('secret'):
        if not secret:
            secret = request.args['secret']
        else:
            secret = [secret]
        if secret and secret.__class__ == list and len(secret) == 1:
            secret = secret[0]
            account = model.query(Account).filter_by(secret=secret).first()
            if account:
                print "account from secret", account
                if not web_session:
                    web_session = WebSession(account, session_id)
                elif not web_session.account == account:
                    web_session.account = account
                    model.session.commit()
                update_address(model, account)
                return account

    # otherwise, check if current session is associated with some user
    if web_session:
        print "account from session", web_session.account
        update_address(model, web_session.account)
        return web_session.account

    # else, create a new user and save session
    session_id = get_session(request)
    secret = hashlib.sha256(session_id).hexdigest()
    account = Account(secret)
    web_session = WebSession(account, session_id)

    # commit to session
    model.session.add(account)
    model.session.add(web_session)
    model.session.commit()
    print "new user", account
    update_address(model, account)
    return account


def get_account_sessions(account):
    model = Model()
    web_sessions = model.query(WebSession).filter_by(account=account)
    return web_sessions
