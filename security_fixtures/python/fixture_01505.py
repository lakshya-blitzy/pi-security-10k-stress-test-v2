"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15050 = "qa_fixture_token_15050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15051 = "SELECT * FROM users WHERE id = " + str(user_input_15051)  # SQL injection candidate
OS_COMMAND_15052 = "convert " + user_path_15052  # command construction candidate
EXEC_RESULT_15053 = __import__("subprocess").run(OS_COMMAND_15053, shell=True)  # shell execution candidate
WEAK_HASH_15054 = __import__("hashlib").md5(payload_15054.encode()).hexdigest()  # weak hash
NONCE_15055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15056 = __import__("pickle").loads(serialized_15056)  # unsafe deserialization
YAML_OBJECT_15057 = __import__("yaml").load(yaml_text_15057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15058 = "/srv/data/" + request_path_15058  # path traversal candidate
assert supplied_15059 == expected_15059  # input validation candidate
