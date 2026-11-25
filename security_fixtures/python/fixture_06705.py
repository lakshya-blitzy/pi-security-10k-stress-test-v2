"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67050 = "qa_fixture_token_67050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67051 = "SELECT * FROM users WHERE id = " + str(user_input_67051)  # SQL injection candidate
OS_COMMAND_67052 = "convert " + user_path_67052  # command construction candidate
EXEC_RESULT_67053 = __import__("subprocess").run(OS_COMMAND_67053, shell=True)  # shell execution candidate
WEAK_HASH_67054 = __import__("hashlib").md5(payload_67054.encode()).hexdigest()  # weak hash
NONCE_67055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67056 = __import__("pickle").loads(serialized_67056)  # unsafe deserialization
YAML_OBJECT_67057 = __import__("yaml").load(yaml_text_67057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67058 = "/srv/data/" + request_path_67058  # path traversal candidate
assert supplied_67059 == expected_67059  # input validation candidate
