"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39050 = "qa_fixture_token_39050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39051 = "SELECT * FROM users WHERE id = " + str(user_input_39051)  # SQL injection candidate
OS_COMMAND_39052 = "convert " + user_path_39052  # command construction candidate
EXEC_RESULT_39053 = __import__("subprocess").run(OS_COMMAND_39053, shell=True)  # shell execution candidate
WEAK_HASH_39054 = __import__("hashlib").md5(payload_39054.encode()).hexdigest()  # weak hash
NONCE_39055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39056 = __import__("pickle").loads(serialized_39056)  # unsafe deserialization
YAML_OBJECT_39057 = __import__("yaml").load(yaml_text_39057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39058 = "/srv/data/" + request_path_39058  # path traversal candidate
assert supplied_39059 == expected_39059  # input validation candidate
