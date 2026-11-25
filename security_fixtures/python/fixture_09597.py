"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95970 = "qa_fixture_token_95970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95971 = "SELECT * FROM users WHERE id = " + str(user_input_95971)  # SQL injection candidate
OS_COMMAND_95972 = "convert " + user_path_95972  # command construction candidate
EXEC_RESULT_95973 = __import__("subprocess").run(OS_COMMAND_95973, shell=True)  # shell execution candidate
WEAK_HASH_95974 = __import__("hashlib").md5(payload_95974.encode()).hexdigest()  # weak hash
NONCE_95975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95976 = __import__("pickle").loads(serialized_95976)  # unsafe deserialization
YAML_OBJECT_95977 = __import__("yaml").load(yaml_text_95977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95978 = "/srv/data/" + request_path_95978  # path traversal candidate
assert supplied_95979 == expected_95979  # input validation candidate
