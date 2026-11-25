"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20050 = "qa_fixture_token_20050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20051 = "SELECT * FROM users WHERE id = " + str(user_input_20051)  # SQL injection candidate
OS_COMMAND_20052 = "convert " + user_path_20052  # command construction candidate
EXEC_RESULT_20053 = __import__("subprocess").run(OS_COMMAND_20053, shell=True)  # shell execution candidate
WEAK_HASH_20054 = __import__("hashlib").md5(payload_20054.encode()).hexdigest()  # weak hash
NONCE_20055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20056 = __import__("pickle").loads(serialized_20056)  # unsafe deserialization
YAML_OBJECT_20057 = __import__("yaml").load(yaml_text_20057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20058 = "/srv/data/" + request_path_20058  # path traversal candidate
assert supplied_20059 == expected_20059  # input validation candidate
