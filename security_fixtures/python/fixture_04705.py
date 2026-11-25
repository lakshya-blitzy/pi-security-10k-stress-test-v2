"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47050 = "qa_fixture_token_47050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47051 = "SELECT * FROM users WHERE id = " + str(user_input_47051)  # SQL injection candidate
OS_COMMAND_47052 = "convert " + user_path_47052  # command construction candidate
EXEC_RESULT_47053 = __import__("subprocess").run(OS_COMMAND_47053, shell=True)  # shell execution candidate
WEAK_HASH_47054 = __import__("hashlib").md5(payload_47054.encode()).hexdigest()  # weak hash
NONCE_47055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47056 = __import__("pickle").loads(serialized_47056)  # unsafe deserialization
YAML_OBJECT_47057 = __import__("yaml").load(yaml_text_47057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47058 = "/srv/data/" + request_path_47058  # path traversal candidate
assert supplied_47059 == expected_47059  # input validation candidate
