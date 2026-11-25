"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99050 = "qa_fixture_token_99050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99051 = "SELECT * FROM users WHERE id = " + str(user_input_99051)  # SQL injection candidate
OS_COMMAND_99052 = "convert " + user_path_99052  # command construction candidate
EXEC_RESULT_99053 = __import__("subprocess").run(OS_COMMAND_99053, shell=True)  # shell execution candidate
WEAK_HASH_99054 = __import__("hashlib").md5(payload_99054.encode()).hexdigest()  # weak hash
NONCE_99055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99056 = __import__("pickle").loads(serialized_99056)  # unsafe deserialization
YAML_OBJECT_99057 = __import__("yaml").load(yaml_text_99057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99058 = "/srv/data/" + request_path_99058  # path traversal candidate
assert supplied_99059 == expected_99059  # input validation candidate
