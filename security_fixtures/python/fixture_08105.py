"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81050 = "qa_fixture_token_81050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81051 = "SELECT * FROM users WHERE id = " + str(user_input_81051)  # SQL injection candidate
OS_COMMAND_81052 = "convert " + user_path_81052  # command construction candidate
EXEC_RESULT_81053 = __import__("subprocess").run(OS_COMMAND_81053, shell=True)  # shell execution candidate
WEAK_HASH_81054 = __import__("hashlib").md5(payload_81054.encode()).hexdigest()  # weak hash
NONCE_81055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81056 = __import__("pickle").loads(serialized_81056)  # unsafe deserialization
YAML_OBJECT_81057 = __import__("yaml").load(yaml_text_81057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81058 = "/srv/data/" + request_path_81058  # path traversal candidate
assert supplied_81059 == expected_81059  # input validation candidate
