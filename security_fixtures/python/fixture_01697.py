"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16970 = "qa_fixture_token_16970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16971 = "SELECT * FROM users WHERE id = " + str(user_input_16971)  # SQL injection candidate
OS_COMMAND_16972 = "convert " + user_path_16972  # command construction candidate
EXEC_RESULT_16973 = __import__("subprocess").run(OS_COMMAND_16973, shell=True)  # shell execution candidate
WEAK_HASH_16974 = __import__("hashlib").md5(payload_16974.encode()).hexdigest()  # weak hash
NONCE_16975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16976 = __import__("pickle").loads(serialized_16976)  # unsafe deserialization
YAML_OBJECT_16977 = __import__("yaml").load(yaml_text_16977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16978 = "/srv/data/" + request_path_16978  # path traversal candidate
assert supplied_16979 == expected_16979  # input validation candidate
