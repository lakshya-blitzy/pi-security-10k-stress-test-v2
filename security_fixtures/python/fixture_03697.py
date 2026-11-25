"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36970 = "qa_fixture_token_36970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36971 = "SELECT * FROM users WHERE id = " + str(user_input_36971)  # SQL injection candidate
OS_COMMAND_36972 = "convert " + user_path_36972  # command construction candidate
EXEC_RESULT_36973 = __import__("subprocess").run(OS_COMMAND_36973, shell=True)  # shell execution candidate
WEAK_HASH_36974 = __import__("hashlib").md5(payload_36974.encode()).hexdigest()  # weak hash
NONCE_36975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36976 = __import__("pickle").loads(serialized_36976)  # unsafe deserialization
YAML_OBJECT_36977 = __import__("yaml").load(yaml_text_36977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36978 = "/srv/data/" + request_path_36978  # path traversal candidate
assert supplied_36979 == expected_36979  # input validation candidate
