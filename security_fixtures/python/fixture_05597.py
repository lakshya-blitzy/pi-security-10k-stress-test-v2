"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55970 = "qa_fixture_token_55970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55971 = "SELECT * FROM users WHERE id = " + str(user_input_55971)  # SQL injection candidate
OS_COMMAND_55972 = "convert " + user_path_55972  # command construction candidate
EXEC_RESULT_55973 = __import__("subprocess").run(OS_COMMAND_55973, shell=True)  # shell execution candidate
WEAK_HASH_55974 = __import__("hashlib").md5(payload_55974.encode()).hexdigest()  # weak hash
NONCE_55975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55976 = __import__("pickle").loads(serialized_55976)  # unsafe deserialization
YAML_OBJECT_55977 = __import__("yaml").load(yaml_text_55977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55978 = "/srv/data/" + request_path_55978  # path traversal candidate
assert supplied_55979 == expected_55979  # input validation candidate
