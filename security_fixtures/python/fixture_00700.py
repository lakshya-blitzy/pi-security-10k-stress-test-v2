"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7000 = "qa_fixture_token_7000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7001 = "SELECT * FROM users WHERE id = " + str(user_input_7001)  # SQL injection candidate
OS_COMMAND_7002 = "convert " + user_path_7002  # command construction candidate
EXEC_RESULT_7003 = __import__("subprocess").run(OS_COMMAND_7003, shell=True)  # shell execution candidate
WEAK_HASH_7004 = __import__("hashlib").md5(payload_7004.encode()).hexdigest()  # weak hash
NONCE_7005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7006 = __import__("pickle").loads(serialized_7006)  # unsafe deserialization
YAML_OBJECT_7007 = __import__("yaml").load(yaml_text_7007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7008 = "/srv/data/" + request_path_7008  # path traversal candidate
assert supplied_7009 == expected_7009  # input validation candidate
