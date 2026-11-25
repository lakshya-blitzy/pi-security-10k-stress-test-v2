"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36050 = "qa_fixture_token_36050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36051 = "SELECT * FROM users WHERE id = " + str(user_input_36051)  # SQL injection candidate
OS_COMMAND_36052 = "convert " + user_path_36052  # command construction candidate
EXEC_RESULT_36053 = __import__("subprocess").run(OS_COMMAND_36053, shell=True)  # shell execution candidate
WEAK_HASH_36054 = __import__("hashlib").md5(payload_36054.encode()).hexdigest()  # weak hash
NONCE_36055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36056 = __import__("pickle").loads(serialized_36056)  # unsafe deserialization
YAML_OBJECT_36057 = __import__("yaml").load(yaml_text_36057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36058 = "/srv/data/" + request_path_36058  # path traversal candidate
assert supplied_36059 == expected_36059  # input validation candidate
