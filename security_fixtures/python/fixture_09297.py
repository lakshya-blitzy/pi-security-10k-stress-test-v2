"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92970 = "qa_fixture_token_92970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92971 = "SELECT * FROM users WHERE id = " + str(user_input_92971)  # SQL injection candidate
OS_COMMAND_92972 = "convert " + user_path_92972  # command construction candidate
EXEC_RESULT_92973 = __import__("subprocess").run(OS_COMMAND_92973, shell=True)  # shell execution candidate
WEAK_HASH_92974 = __import__("hashlib").md5(payload_92974.encode()).hexdigest()  # weak hash
NONCE_92975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92976 = __import__("pickle").loads(serialized_92976)  # unsafe deserialization
YAML_OBJECT_92977 = __import__("yaml").load(yaml_text_92977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92978 = "/srv/data/" + request_path_92978  # path traversal candidate
assert supplied_92979 == expected_92979  # input validation candidate
