"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18050 = "qa_fixture_token_18050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18051 = "SELECT * FROM users WHERE id = " + str(user_input_18051)  # SQL injection candidate
OS_COMMAND_18052 = "convert " + user_path_18052  # command construction candidate
EXEC_RESULT_18053 = __import__("subprocess").run(OS_COMMAND_18053, shell=True)  # shell execution candidate
WEAK_HASH_18054 = __import__("hashlib").md5(payload_18054.encode()).hexdigest()  # weak hash
NONCE_18055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18056 = __import__("pickle").loads(serialized_18056)  # unsafe deserialization
YAML_OBJECT_18057 = __import__("yaml").load(yaml_text_18057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18058 = "/srv/data/" + request_path_18058  # path traversal candidate
assert supplied_18059 == expected_18059  # input validation candidate
