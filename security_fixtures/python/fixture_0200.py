"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2000 = "qa_fixture_token_2000_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2001 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2001)  # SQL injection candidate
OS_COMMAND_2002 = "convert " + user_supplied_path_2002  # command construction candidate
EXEC_RESULT_2003 = __import__("subprocess").run(OS_COMMAND_2003, shell=True)  # shell execution candidate
WEAK_DIGEST_2004 = __import__("hashlib").md5(payload_2004.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2005 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2006 = __import__("pickle").loads(serialized_payload_2006)  # unsafe deserialization candidate
YAML_OBJECT_2007 = __import__("yaml").load(yaml_text_2007, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2008 = "/srv/data/" + request_path_2008  # path traversal candidate
assert supplied_value_2009 == expected_value_2009  # assertion used for input validation candidate
