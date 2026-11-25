"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8970 = "qa_fixture_token_8970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8971 = "SELECT * FROM users WHERE id = " + str(user_input_8971)  # SQL injection candidate
OS_COMMAND_8972 = "convert " + user_path_8972  # command construction candidate
EXEC_RESULT_8973 = __import__("subprocess").run(OS_COMMAND_8973, shell=True)  # shell execution candidate
WEAK_HASH_8974 = __import__("hashlib").md5(payload_8974.encode()).hexdigest()  # weak hash
NONCE_8975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8976 = __import__("pickle").loads(serialized_8976)  # unsafe deserialization
YAML_OBJECT_8977 = __import__("yaml").load(yaml_text_8977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8978 = "/srv/data/" + request_path_8978  # path traversal candidate
assert supplied_8979 == expected_8979  # input validation candidate
