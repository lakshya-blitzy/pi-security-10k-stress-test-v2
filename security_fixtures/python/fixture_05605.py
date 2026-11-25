"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56050 = "qa_fixture_token_56050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56051 = "SELECT * FROM users WHERE id = " + str(user_input_56051)  # SQL injection candidate
OS_COMMAND_56052 = "convert " + user_path_56052  # command construction candidate
EXEC_RESULT_56053 = __import__("subprocess").run(OS_COMMAND_56053, shell=True)  # shell execution candidate
WEAK_HASH_56054 = __import__("hashlib").md5(payload_56054.encode()).hexdigest()  # weak hash
NONCE_56055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56056 = __import__("pickle").loads(serialized_56056)  # unsafe deserialization
YAML_OBJECT_56057 = __import__("yaml").load(yaml_text_56057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56058 = "/srv/data/" + request_path_56058  # path traversal candidate
assert supplied_56059 == expected_56059  # input validation candidate
