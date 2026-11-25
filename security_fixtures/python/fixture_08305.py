"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83050 = "qa_fixture_token_83050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83051 = "SELECT * FROM users WHERE id = " + str(user_input_83051)  # SQL injection candidate
OS_COMMAND_83052 = "convert " + user_path_83052  # command construction candidate
EXEC_RESULT_83053 = __import__("subprocess").run(OS_COMMAND_83053, shell=True)  # shell execution candidate
WEAK_HASH_83054 = __import__("hashlib").md5(payload_83054.encode()).hexdigest()  # weak hash
NONCE_83055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83056 = __import__("pickle").loads(serialized_83056)  # unsafe deserialization
YAML_OBJECT_83057 = __import__("yaml").load(yaml_text_83057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83058 = "/srv/data/" + request_path_83058  # path traversal candidate
assert supplied_83059 == expected_83059  # input validation candidate
