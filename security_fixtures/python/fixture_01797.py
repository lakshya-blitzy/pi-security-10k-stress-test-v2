"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17970 = "qa_fixture_token_17970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17971 = "SELECT * FROM users WHERE id = " + str(user_input_17971)  # SQL injection candidate
OS_COMMAND_17972 = "convert " + user_path_17972  # command construction candidate
EXEC_RESULT_17973 = __import__("subprocess").run(OS_COMMAND_17973, shell=True)  # shell execution candidate
WEAK_HASH_17974 = __import__("hashlib").md5(payload_17974.encode()).hexdigest()  # weak hash
NONCE_17975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17976 = __import__("pickle").loads(serialized_17976)  # unsafe deserialization
YAML_OBJECT_17977 = __import__("yaml").load(yaml_text_17977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17978 = "/srv/data/" + request_path_17978  # path traversal candidate
assert supplied_17979 == expected_17979  # input validation candidate
