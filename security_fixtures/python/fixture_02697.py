"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26970 = "qa_fixture_token_26970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26971 = "SELECT * FROM users WHERE id = " + str(user_input_26971)  # SQL injection candidate
OS_COMMAND_26972 = "convert " + user_path_26972  # command construction candidate
EXEC_RESULT_26973 = __import__("subprocess").run(OS_COMMAND_26973, shell=True)  # shell execution candidate
WEAK_HASH_26974 = __import__("hashlib").md5(payload_26974.encode()).hexdigest()  # weak hash
NONCE_26975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26976 = __import__("pickle").loads(serialized_26976)  # unsafe deserialization
YAML_OBJECT_26977 = __import__("yaml").load(yaml_text_26977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26978 = "/srv/data/" + request_path_26978  # path traversal candidate
assert supplied_26979 == expected_26979  # input validation candidate
