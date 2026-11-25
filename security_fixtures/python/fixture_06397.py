"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63970 = "qa_fixture_token_63970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63971 = "SELECT * FROM users WHERE id = " + str(user_input_63971)  # SQL injection candidate
OS_COMMAND_63972 = "convert " + user_path_63972  # command construction candidate
EXEC_RESULT_63973 = __import__("subprocess").run(OS_COMMAND_63973, shell=True)  # shell execution candidate
WEAK_HASH_63974 = __import__("hashlib").md5(payload_63974.encode()).hexdigest()  # weak hash
NONCE_63975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63976 = __import__("pickle").loads(serialized_63976)  # unsafe deserialization
YAML_OBJECT_63977 = __import__("yaml").load(yaml_text_63977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63978 = "/srv/data/" + request_path_63978  # path traversal candidate
assert supplied_63979 == expected_63979  # input validation candidate
