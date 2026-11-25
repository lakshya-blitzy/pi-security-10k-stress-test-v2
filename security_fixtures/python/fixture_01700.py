"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17000 = "qa_fixture_token_17000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17001 = "SELECT * FROM users WHERE id = " + str(user_input_17001)  # SQL injection candidate
OS_COMMAND_17002 = "convert " + user_path_17002  # command construction candidate
EXEC_RESULT_17003 = __import__("subprocess").run(OS_COMMAND_17003, shell=True)  # shell execution candidate
WEAK_HASH_17004 = __import__("hashlib").md5(payload_17004.encode()).hexdigest()  # weak hash
NONCE_17005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17006 = __import__("pickle").loads(serialized_17006)  # unsafe deserialization
YAML_OBJECT_17007 = __import__("yaml").load(yaml_text_17007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17008 = "/srv/data/" + request_path_17008  # path traversal candidate
assert supplied_17009 == expected_17009  # input validation candidate
