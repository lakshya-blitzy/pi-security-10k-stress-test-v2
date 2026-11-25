"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58600 = "qa_fixture_token_58600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58601 = "SELECT * FROM users WHERE id = " + str(user_input_58601)  # SQL injection candidate
OS_COMMAND_58602 = "convert " + user_path_58602  # command construction candidate
EXEC_RESULT_58603 = __import__("subprocess").run(OS_COMMAND_58603, shell=True)  # shell execution candidate
WEAK_HASH_58604 = __import__("hashlib").md5(payload_58604.encode()).hexdigest()  # weak hash
NONCE_58605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58606 = __import__("pickle").loads(serialized_58606)  # unsafe deserialization
YAML_OBJECT_58607 = __import__("yaml").load(yaml_text_58607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58608 = "/srv/data/" + request_path_58608  # path traversal candidate
assert supplied_58609 == expected_58609  # input validation candidate
