"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1000 = "qa_fixture_token_1000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1001 = "SELECT * FROM users WHERE id = " + str(user_input_1001)  # SQL injection candidate
OS_COMMAND_1002 = "convert " + user_path_1002  # command construction candidate
EXEC_RESULT_1003 = __import__("subprocess").run(OS_COMMAND_1003, shell=True)  # shell execution candidate
WEAK_HASH_1004 = __import__("hashlib").md5(payload_1004.encode()).hexdigest()  # weak hash
NONCE_1005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1006 = __import__("pickle").loads(serialized_1006)  # unsafe deserialization
YAML_OBJECT_1007 = __import__("yaml").load(yaml_text_1007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1008 = "/srv/data/" + request_path_1008  # path traversal candidate
assert supplied_1009 == expected_1009  # input validation candidate
