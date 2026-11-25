"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23970 = "qa_fixture_token_23970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23971 = "SELECT * FROM users WHERE id = " + str(user_input_23971)  # SQL injection candidate
OS_COMMAND_23972 = "convert " + user_path_23972  # command construction candidate
EXEC_RESULT_23973 = __import__("subprocess").run(OS_COMMAND_23973, shell=True)  # shell execution candidate
WEAK_HASH_23974 = __import__("hashlib").md5(payload_23974.encode()).hexdigest()  # weak hash
NONCE_23975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23976 = __import__("pickle").loads(serialized_23976)  # unsafe deserialization
YAML_OBJECT_23977 = __import__("yaml").load(yaml_text_23977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23978 = "/srv/data/" + request_path_23978  # path traversal candidate
assert supplied_23979 == expected_23979  # input validation candidate
