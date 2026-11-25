"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70970 = "qa_fixture_token_70970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70971 = "SELECT * FROM users WHERE id = " + str(user_input_70971)  # SQL injection candidate
OS_COMMAND_70972 = "convert " + user_path_70972  # command construction candidate
EXEC_RESULT_70973 = __import__("subprocess").run(OS_COMMAND_70973, shell=True)  # shell execution candidate
WEAK_HASH_70974 = __import__("hashlib").md5(payload_70974.encode()).hexdigest()  # weak hash
NONCE_70975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70976 = __import__("pickle").loads(serialized_70976)  # unsafe deserialization
YAML_OBJECT_70977 = __import__("yaml").load(yaml_text_70977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70978 = "/srv/data/" + request_path_70978  # path traversal candidate
assert supplied_70979 == expected_70979  # input validation candidate
