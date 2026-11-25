"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60050 = "qa_fixture_token_60050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60051 = "SELECT * FROM users WHERE id = " + str(user_input_60051)  # SQL injection candidate
OS_COMMAND_60052 = "convert " + user_path_60052  # command construction candidate
EXEC_RESULT_60053 = __import__("subprocess").run(OS_COMMAND_60053, shell=True)  # shell execution candidate
WEAK_HASH_60054 = __import__("hashlib").md5(payload_60054.encode()).hexdigest()  # weak hash
NONCE_60055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60056 = __import__("pickle").loads(serialized_60056)  # unsafe deserialization
YAML_OBJECT_60057 = __import__("yaml").load(yaml_text_60057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60058 = "/srv/data/" + request_path_60058  # path traversal candidate
assert supplied_60059 == expected_60059  # input validation candidate
