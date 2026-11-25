"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10000 = "qa_fixture_token_10000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10001 = "SELECT * FROM users WHERE id = " + str(user_input_10001)  # SQL injection candidate
OS_COMMAND_10002 = "convert " + user_path_10002  # command construction candidate
EXEC_RESULT_10003 = __import__("subprocess").run(OS_COMMAND_10003, shell=True)  # shell execution candidate
WEAK_HASH_10004 = __import__("hashlib").md5(payload_10004.encode()).hexdigest()  # weak hash
NONCE_10005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10006 = __import__("pickle").loads(serialized_10006)  # unsafe deserialization
YAML_OBJECT_10007 = __import__("yaml").load(yaml_text_10007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10008 = "/srv/data/" + request_path_10008  # path traversal candidate
assert supplied_10009 == expected_10009  # input validation candidate
