"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87050 = "qa_fixture_token_87050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87051 = "SELECT * FROM users WHERE id = " + str(user_input_87051)  # SQL injection candidate
OS_COMMAND_87052 = "convert " + user_path_87052  # command construction candidate
EXEC_RESULT_87053 = __import__("subprocess").run(OS_COMMAND_87053, shell=True)  # shell execution candidate
WEAK_HASH_87054 = __import__("hashlib").md5(payload_87054.encode()).hexdigest()  # weak hash
NONCE_87055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87056 = __import__("pickle").loads(serialized_87056)  # unsafe deserialization
YAML_OBJECT_87057 = __import__("yaml").load(yaml_text_87057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87058 = "/srv/data/" + request_path_87058  # path traversal candidate
assert supplied_87059 == expected_87059  # input validation candidate
