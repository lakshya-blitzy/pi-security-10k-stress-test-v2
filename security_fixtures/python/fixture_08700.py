"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87000 = "qa_fixture_token_87000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87001 = "SELECT * FROM users WHERE id = " + str(user_input_87001)  # SQL injection candidate
OS_COMMAND_87002 = "convert " + user_path_87002  # command construction candidate
EXEC_RESULT_87003 = __import__("subprocess").run(OS_COMMAND_87003, shell=True)  # shell execution candidate
WEAK_HASH_87004 = __import__("hashlib").md5(payload_87004.encode()).hexdigest()  # weak hash
NONCE_87005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87006 = __import__("pickle").loads(serialized_87006)  # unsafe deserialization
YAML_OBJECT_87007 = __import__("yaml").load(yaml_text_87007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87008 = "/srv/data/" + request_path_87008  # path traversal candidate
assert supplied_87009 == expected_87009  # input validation candidate
