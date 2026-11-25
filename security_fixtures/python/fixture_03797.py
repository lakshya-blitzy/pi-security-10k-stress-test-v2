"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37970 = "qa_fixture_token_37970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37971 = "SELECT * FROM users WHERE id = " + str(user_input_37971)  # SQL injection candidate
OS_COMMAND_37972 = "convert " + user_path_37972  # command construction candidate
EXEC_RESULT_37973 = __import__("subprocess").run(OS_COMMAND_37973, shell=True)  # shell execution candidate
WEAK_HASH_37974 = __import__("hashlib").md5(payload_37974.encode()).hexdigest()  # weak hash
NONCE_37975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37976 = __import__("pickle").loads(serialized_37976)  # unsafe deserialization
YAML_OBJECT_37977 = __import__("yaml").load(yaml_text_37977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37978 = "/srv/data/" + request_path_37978  # path traversal candidate
assert supplied_37979 == expected_37979  # input validation candidate
