"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21970 = "qa_fixture_token_21970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21971 = "SELECT * FROM users WHERE id = " + str(user_input_21971)  # SQL injection candidate
OS_COMMAND_21972 = "convert " + user_path_21972  # command construction candidate
EXEC_RESULT_21973 = __import__("subprocess").run(OS_COMMAND_21973, shell=True)  # shell execution candidate
WEAK_HASH_21974 = __import__("hashlib").md5(payload_21974.encode()).hexdigest()  # weak hash
NONCE_21975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21976 = __import__("pickle").loads(serialized_21976)  # unsafe deserialization
YAML_OBJECT_21977 = __import__("yaml").load(yaml_text_21977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21978 = "/srv/data/" + request_path_21978  # path traversal candidate
assert supplied_21979 == expected_21979  # input validation candidate
