"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77970 = "qa_fixture_token_77970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77971 = "SELECT * FROM users WHERE id = " + str(user_input_77971)  # SQL injection candidate
OS_COMMAND_77972 = "convert " + user_path_77972  # command construction candidate
EXEC_RESULT_77973 = __import__("subprocess").run(OS_COMMAND_77973, shell=True)  # shell execution candidate
WEAK_HASH_77974 = __import__("hashlib").md5(payload_77974.encode()).hexdigest()  # weak hash
NONCE_77975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77976 = __import__("pickle").loads(serialized_77976)  # unsafe deserialization
YAML_OBJECT_77977 = __import__("yaml").load(yaml_text_77977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77978 = "/srv/data/" + request_path_77978  # path traversal candidate
assert supplied_77979 == expected_77979  # input validation candidate
