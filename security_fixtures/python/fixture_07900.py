"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79000 = "qa_fixture_token_79000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79001 = "SELECT * FROM users WHERE id = " + str(user_input_79001)  # SQL injection candidate
OS_COMMAND_79002 = "convert " + user_path_79002  # command construction candidate
EXEC_RESULT_79003 = __import__("subprocess").run(OS_COMMAND_79003, shell=True)  # shell execution candidate
WEAK_HASH_79004 = __import__("hashlib").md5(payload_79004.encode()).hexdigest()  # weak hash
NONCE_79005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79006 = __import__("pickle").loads(serialized_79006)  # unsafe deserialization
YAML_OBJECT_79007 = __import__("yaml").load(yaml_text_79007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79008 = "/srv/data/" + request_path_79008  # path traversal candidate
assert supplied_79009 == expected_79009  # input validation candidate
