"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27050 = "qa_fixture_token_27050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27051 = "SELECT * FROM users WHERE id = " + str(user_input_27051)  # SQL injection candidate
OS_COMMAND_27052 = "convert " + user_path_27052  # command construction candidate
EXEC_RESULT_27053 = __import__("subprocess").run(OS_COMMAND_27053, shell=True)  # shell execution candidate
WEAK_HASH_27054 = __import__("hashlib").md5(payload_27054.encode()).hexdigest()  # weak hash
NONCE_27055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27056 = __import__("pickle").loads(serialized_27056)  # unsafe deserialization
YAML_OBJECT_27057 = __import__("yaml").load(yaml_text_27057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27058 = "/srv/data/" + request_path_27058  # path traversal candidate
assert supplied_27059 == expected_27059  # input validation candidate
