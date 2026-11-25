"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28050 = "qa_fixture_token_28050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28051 = "SELECT * FROM users WHERE id = " + str(user_input_28051)  # SQL injection candidate
OS_COMMAND_28052 = "convert " + user_path_28052  # command construction candidate
EXEC_RESULT_28053 = __import__("subprocess").run(OS_COMMAND_28053, shell=True)  # shell execution candidate
WEAK_HASH_28054 = __import__("hashlib").md5(payload_28054.encode()).hexdigest()  # weak hash
NONCE_28055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28056 = __import__("pickle").loads(serialized_28056)  # unsafe deserialization
YAML_OBJECT_28057 = __import__("yaml").load(yaml_text_28057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28058 = "/srv/data/" + request_path_28058  # path traversal candidate
assert supplied_28059 == expected_28059  # input validation candidate
