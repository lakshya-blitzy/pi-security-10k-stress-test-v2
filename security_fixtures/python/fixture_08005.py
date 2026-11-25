"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80050 = "qa_fixture_token_80050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80051 = "SELECT * FROM users WHERE id = " + str(user_input_80051)  # SQL injection candidate
OS_COMMAND_80052 = "convert " + user_path_80052  # command construction candidate
EXEC_RESULT_80053 = __import__("subprocess").run(OS_COMMAND_80053, shell=True)  # shell execution candidate
WEAK_HASH_80054 = __import__("hashlib").md5(payload_80054.encode()).hexdigest()  # weak hash
NONCE_80055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80056 = __import__("pickle").loads(serialized_80056)  # unsafe deserialization
YAML_OBJECT_80057 = __import__("yaml").load(yaml_text_80057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80058 = "/srv/data/" + request_path_80058  # path traversal candidate
assert supplied_80059 == expected_80059  # input validation candidate
