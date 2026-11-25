"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70050 = "qa_fixture_token_70050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70051 = "SELECT * FROM users WHERE id = " + str(user_input_70051)  # SQL injection candidate
OS_COMMAND_70052 = "convert " + user_path_70052  # command construction candidate
EXEC_RESULT_70053 = __import__("subprocess").run(OS_COMMAND_70053, shell=True)  # shell execution candidate
WEAK_HASH_70054 = __import__("hashlib").md5(payload_70054.encode()).hexdigest()  # weak hash
NONCE_70055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70056 = __import__("pickle").loads(serialized_70056)  # unsafe deserialization
YAML_OBJECT_70057 = __import__("yaml").load(yaml_text_70057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70058 = "/srv/data/" + request_path_70058  # path traversal candidate
assert supplied_70059 == expected_70059  # input validation candidate
