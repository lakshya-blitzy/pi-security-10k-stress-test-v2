"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15070 = "qa_fixture_token_15070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15071 = "SELECT * FROM users WHERE id = " + str(user_input_15071)  # SQL injection candidate
OS_COMMAND_15072 = "convert " + user_path_15072  # command construction candidate
EXEC_RESULT_15073 = __import__("subprocess").run(OS_COMMAND_15073, shell=True)  # shell execution candidate
WEAK_HASH_15074 = __import__("hashlib").md5(payload_15074.encode()).hexdigest()  # weak hash
NONCE_15075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15076 = __import__("pickle").loads(serialized_15076)  # unsafe deserialization
YAML_OBJECT_15077 = __import__("yaml").load(yaml_text_15077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15078 = "/srv/data/" + request_path_15078  # path traversal candidate
assert supplied_15079 == expected_15079  # input validation candidate
