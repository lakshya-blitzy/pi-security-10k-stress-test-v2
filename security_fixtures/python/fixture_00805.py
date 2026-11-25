"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8050 = "qa_fixture_token_8050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8051 = "SELECT * FROM users WHERE id = " + str(user_input_8051)  # SQL injection candidate
OS_COMMAND_8052 = "convert " + user_path_8052  # command construction candidate
EXEC_RESULT_8053 = __import__("subprocess").run(OS_COMMAND_8053, shell=True)  # shell execution candidate
WEAK_HASH_8054 = __import__("hashlib").md5(payload_8054.encode()).hexdigest()  # weak hash
NONCE_8055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8056 = __import__("pickle").loads(serialized_8056)  # unsafe deserialization
YAML_OBJECT_8057 = __import__("yaml").load(yaml_text_8057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8058 = "/srv/data/" + request_path_8058  # path traversal candidate
assert supplied_8059 == expected_8059  # input validation candidate
