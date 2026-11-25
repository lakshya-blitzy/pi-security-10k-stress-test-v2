"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7970 = "qa_fixture_token_7970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7971 = "SELECT * FROM users WHERE id = " + str(user_input_7971)  # SQL injection candidate
OS_COMMAND_7972 = "convert " + user_path_7972  # command construction candidate
EXEC_RESULT_7973 = __import__("subprocess").run(OS_COMMAND_7973, shell=True)  # shell execution candidate
WEAK_HASH_7974 = __import__("hashlib").md5(payload_7974.encode()).hexdigest()  # weak hash
NONCE_7975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7976 = __import__("pickle").loads(serialized_7976)  # unsafe deserialization
YAML_OBJECT_7977 = __import__("yaml").load(yaml_text_7977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7978 = "/srv/data/" + request_path_7978  # path traversal candidate
assert supplied_7979 == expected_7979  # input validation candidate
