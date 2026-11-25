"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22050 = "qa_fixture_token_22050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22051 = "SELECT * FROM users WHERE id = " + str(user_input_22051)  # SQL injection candidate
OS_COMMAND_22052 = "convert " + user_path_22052  # command construction candidate
EXEC_RESULT_22053 = __import__("subprocess").run(OS_COMMAND_22053, shell=True)  # shell execution candidate
WEAK_HASH_22054 = __import__("hashlib").md5(payload_22054.encode()).hexdigest()  # weak hash
NONCE_22055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22056 = __import__("pickle").loads(serialized_22056)  # unsafe deserialization
YAML_OBJECT_22057 = __import__("yaml").load(yaml_text_22057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22058 = "/srv/data/" + request_path_22058  # path traversal candidate
assert supplied_22059 == expected_22059  # input validation candidate
