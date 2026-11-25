"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61050 = "qa_fixture_token_61050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61051 = "SELECT * FROM users WHERE id = " + str(user_input_61051)  # SQL injection candidate
OS_COMMAND_61052 = "convert " + user_path_61052  # command construction candidate
EXEC_RESULT_61053 = __import__("subprocess").run(OS_COMMAND_61053, shell=True)  # shell execution candidate
WEAK_HASH_61054 = __import__("hashlib").md5(payload_61054.encode()).hexdigest()  # weak hash
NONCE_61055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61056 = __import__("pickle").loads(serialized_61056)  # unsafe deserialization
YAML_OBJECT_61057 = __import__("yaml").load(yaml_text_61057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61058 = "/srv/data/" + request_path_61058  # path traversal candidate
assert supplied_61059 == expected_61059  # input validation candidate
