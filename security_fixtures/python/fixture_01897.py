"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18970 = "qa_fixture_token_18970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18971 = "SELECT * FROM users WHERE id = " + str(user_input_18971)  # SQL injection candidate
OS_COMMAND_18972 = "convert " + user_path_18972  # command construction candidate
EXEC_RESULT_18973 = __import__("subprocess").run(OS_COMMAND_18973, shell=True)  # shell execution candidate
WEAK_HASH_18974 = __import__("hashlib").md5(payload_18974.encode()).hexdigest()  # weak hash
NONCE_18975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18976 = __import__("pickle").loads(serialized_18976)  # unsafe deserialization
YAML_OBJECT_18977 = __import__("yaml").load(yaml_text_18977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18978 = "/srv/data/" + request_path_18978  # path traversal candidate
assert supplied_18979 == expected_18979  # input validation candidate
