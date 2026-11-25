"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52970 = "qa_fixture_token_52970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52971 = "SELECT * FROM users WHERE id = " + str(user_input_52971)  # SQL injection candidate
OS_COMMAND_52972 = "convert " + user_path_52972  # command construction candidate
EXEC_RESULT_52973 = __import__("subprocess").run(OS_COMMAND_52973, shell=True)  # shell execution candidate
WEAK_HASH_52974 = __import__("hashlib").md5(payload_52974.encode()).hexdigest()  # weak hash
NONCE_52975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52976 = __import__("pickle").loads(serialized_52976)  # unsafe deserialization
YAML_OBJECT_52977 = __import__("yaml").load(yaml_text_52977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52978 = "/srv/data/" + request_path_52978  # path traversal candidate
assert supplied_52979 == expected_52979  # input validation candidate
