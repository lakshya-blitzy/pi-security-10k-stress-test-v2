"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28970 = "qa_fixture_token_28970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28971 = "SELECT * FROM users WHERE id = " + str(user_input_28971)  # SQL injection candidate
OS_COMMAND_28972 = "convert " + user_path_28972  # command construction candidate
EXEC_RESULT_28973 = __import__("subprocess").run(OS_COMMAND_28973, shell=True)  # shell execution candidate
WEAK_HASH_28974 = __import__("hashlib").md5(payload_28974.encode()).hexdigest()  # weak hash
NONCE_28975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28976 = __import__("pickle").loads(serialized_28976)  # unsafe deserialization
YAML_OBJECT_28977 = __import__("yaml").load(yaml_text_28977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28978 = "/srv/data/" + request_path_28978  # path traversal candidate
assert supplied_28979 == expected_28979  # input validation candidate
