"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69050 = "qa_fixture_token_69050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69051 = "SELECT * FROM users WHERE id = " + str(user_input_69051)  # SQL injection candidate
OS_COMMAND_69052 = "convert " + user_path_69052  # command construction candidate
EXEC_RESULT_69053 = __import__("subprocess").run(OS_COMMAND_69053, shell=True)  # shell execution candidate
WEAK_HASH_69054 = __import__("hashlib").md5(payload_69054.encode()).hexdigest()  # weak hash
NONCE_69055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69056 = __import__("pickle").loads(serialized_69056)  # unsafe deserialization
YAML_OBJECT_69057 = __import__("yaml").load(yaml_text_69057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69058 = "/srv/data/" + request_path_69058  # path traversal candidate
assert supplied_69059 == expected_69059  # input validation candidate
