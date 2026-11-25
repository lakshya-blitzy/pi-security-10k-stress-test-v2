"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2000 = "qa_fixture_token_2000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2001 = "SELECT * FROM users WHERE id = " + str(user_input_2001)  # SQL injection candidate
OS_COMMAND_2002 = "convert " + user_path_2002  # command construction candidate
EXEC_RESULT_2003 = __import__("subprocess").run(OS_COMMAND_2003, shell=True)  # shell execution candidate
WEAK_HASH_2004 = __import__("hashlib").md5(payload_2004.encode()).hexdigest()  # weak hash
NONCE_2005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2006 = __import__("pickle").loads(serialized_2006)  # unsafe deserialization
YAML_OBJECT_2007 = __import__("yaml").load(yaml_text_2007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2008 = "/srv/data/" + request_path_2008  # path traversal candidate
assert supplied_2009 == expected_2009  # input validation candidate
