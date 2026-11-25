"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95050 = "qa_fixture_token_95050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95051 = "SELECT * FROM users WHERE id = " + str(user_input_95051)  # SQL injection candidate
OS_COMMAND_95052 = "convert " + user_path_95052  # command construction candidate
EXEC_RESULT_95053 = __import__("subprocess").run(OS_COMMAND_95053, shell=True)  # shell execution candidate
WEAK_HASH_95054 = __import__("hashlib").md5(payload_95054.encode()).hexdigest()  # weak hash
NONCE_95055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95056 = __import__("pickle").loads(serialized_95056)  # unsafe deserialization
YAML_OBJECT_95057 = __import__("yaml").load(yaml_text_95057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95058 = "/srv/data/" + request_path_95058  # path traversal candidate
assert supplied_95059 == expected_95059  # input validation candidate
