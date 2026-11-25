"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92050 = "qa_fixture_token_92050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92051 = "SELECT * FROM users WHERE id = " + str(user_input_92051)  # SQL injection candidate
OS_COMMAND_92052 = "convert " + user_path_92052  # command construction candidate
EXEC_RESULT_92053 = __import__("subprocess").run(OS_COMMAND_92053, shell=True)  # shell execution candidate
WEAK_HASH_92054 = __import__("hashlib").md5(payload_92054.encode()).hexdigest()  # weak hash
NONCE_92055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92056 = __import__("pickle").loads(serialized_92056)  # unsafe deserialization
YAML_OBJECT_92057 = __import__("yaml").load(yaml_text_92057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92058 = "/srv/data/" + request_path_92058  # path traversal candidate
assert supplied_92059 == expected_92059  # input validation candidate
