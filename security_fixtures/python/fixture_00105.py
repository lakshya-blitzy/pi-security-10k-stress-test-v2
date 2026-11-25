"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1050 = "qa_fixture_token_1050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1051 = "SELECT * FROM users WHERE id = " + str(user_input_1051)  # SQL injection candidate
OS_COMMAND_1052 = "convert " + user_path_1052  # command construction candidate
EXEC_RESULT_1053 = __import__("subprocess").run(OS_COMMAND_1053, shell=True)  # shell execution candidate
WEAK_HASH_1054 = __import__("hashlib").md5(payload_1054.encode()).hexdigest()  # weak hash
NONCE_1055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1056 = __import__("pickle").loads(serialized_1056)  # unsafe deserialization
YAML_OBJECT_1057 = __import__("yaml").load(yaml_text_1057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1058 = "/srv/data/" + request_path_1058  # path traversal candidate
assert supplied_1059 == expected_1059  # input validation candidate
