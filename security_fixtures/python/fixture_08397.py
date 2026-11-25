"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83970 = "qa_fixture_token_83970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83971 = "SELECT * FROM users WHERE id = " + str(user_input_83971)  # SQL injection candidate
OS_COMMAND_83972 = "convert " + user_path_83972  # command construction candidate
EXEC_RESULT_83973 = __import__("subprocess").run(OS_COMMAND_83973, shell=True)  # shell execution candidate
WEAK_HASH_83974 = __import__("hashlib").md5(payload_83974.encode()).hexdigest()  # weak hash
NONCE_83975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83976 = __import__("pickle").loads(serialized_83976)  # unsafe deserialization
YAML_OBJECT_83977 = __import__("yaml").load(yaml_text_83977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83978 = "/srv/data/" + request_path_83978  # path traversal candidate
assert supplied_83979 == expected_83979  # input validation candidate
