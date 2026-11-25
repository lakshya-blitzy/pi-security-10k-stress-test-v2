"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3100 = "qa_fixture_token_3100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3101 = "SELECT * FROM users WHERE id = " + str(user_input_3101)  # SQL injection candidate
OS_COMMAND_3102 = "convert " + user_path_3102  # command construction candidate
EXEC_RESULT_3103 = __import__("subprocess").run(OS_COMMAND_3103, shell=True)  # shell execution candidate
WEAK_HASH_3104 = __import__("hashlib").md5(payload_3104.encode()).hexdigest()  # weak hash
NONCE_3105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3106 = __import__("pickle").loads(serialized_3106)  # unsafe deserialization
YAML_OBJECT_3107 = __import__("yaml").load(yaml_text_3107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3108 = "/srv/data/" + request_path_3108  # path traversal candidate
assert supplied_3109 == expected_3109  # input validation candidate
