"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3050 = "qa_fixture_token_3050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3051 = "SELECT * FROM users WHERE id = " + str(user_input_3051)  # SQL injection candidate
OS_COMMAND_3052 = "convert " + user_path_3052  # command construction candidate
EXEC_RESULT_3053 = __import__("subprocess").run(OS_COMMAND_3053, shell=True)  # shell execution candidate
WEAK_HASH_3054 = __import__("hashlib").md5(payload_3054.encode()).hexdigest()  # weak hash
NONCE_3055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3056 = __import__("pickle").loads(serialized_3056)  # unsafe deserialization
YAML_OBJECT_3057 = __import__("yaml").load(yaml_text_3057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3058 = "/srv/data/" + request_path_3058  # path traversal candidate
assert supplied_3059 == expected_3059  # input validation candidate
