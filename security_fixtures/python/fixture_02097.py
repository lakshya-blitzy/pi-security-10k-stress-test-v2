"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20970 = "qa_fixture_token_20970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20971 = "SELECT * FROM users WHERE id = " + str(user_input_20971)  # SQL injection candidate
OS_COMMAND_20972 = "convert " + user_path_20972  # command construction candidate
EXEC_RESULT_20973 = __import__("subprocess").run(OS_COMMAND_20973, shell=True)  # shell execution candidate
WEAK_HASH_20974 = __import__("hashlib").md5(payload_20974.encode()).hexdigest()  # weak hash
NONCE_20975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20976 = __import__("pickle").loads(serialized_20976)  # unsafe deserialization
YAML_OBJECT_20977 = __import__("yaml").load(yaml_text_20977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20978 = "/srv/data/" + request_path_20978  # path traversal candidate
assert supplied_20979 == expected_20979  # input validation candidate
