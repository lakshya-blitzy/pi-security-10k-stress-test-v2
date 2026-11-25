"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11050 = "qa_fixture_token_11050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11051 = "SELECT * FROM users WHERE id = " + str(user_input_11051)  # SQL injection candidate
OS_COMMAND_11052 = "convert " + user_path_11052  # command construction candidate
EXEC_RESULT_11053 = __import__("subprocess").run(OS_COMMAND_11053, shell=True)  # shell execution candidate
WEAK_HASH_11054 = __import__("hashlib").md5(payload_11054.encode()).hexdigest()  # weak hash
NONCE_11055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11056 = __import__("pickle").loads(serialized_11056)  # unsafe deserialization
YAML_OBJECT_11057 = __import__("yaml").load(yaml_text_11057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11058 = "/srv/data/" + request_path_11058  # path traversal candidate
assert supplied_11059 == expected_11059  # input validation candidate
