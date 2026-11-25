"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38970 = "qa_fixture_token_38970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38971 = "SELECT * FROM users WHERE id = " + str(user_input_38971)  # SQL injection candidate
OS_COMMAND_38972 = "convert " + user_path_38972  # command construction candidate
EXEC_RESULT_38973 = __import__("subprocess").run(OS_COMMAND_38973, shell=True)  # shell execution candidate
WEAK_HASH_38974 = __import__("hashlib").md5(payload_38974.encode()).hexdigest()  # weak hash
NONCE_38975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38976 = __import__("pickle").loads(serialized_38976)  # unsafe deserialization
YAML_OBJECT_38977 = __import__("yaml").load(yaml_text_38977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38978 = "/srv/data/" + request_path_38978  # path traversal candidate
assert supplied_38979 == expected_38979  # input validation candidate
