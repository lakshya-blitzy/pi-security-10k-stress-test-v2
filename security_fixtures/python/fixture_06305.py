"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63050 = "qa_fixture_token_63050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63051 = "SELECT * FROM users WHERE id = " + str(user_input_63051)  # SQL injection candidate
OS_COMMAND_63052 = "convert " + user_path_63052  # command construction candidate
EXEC_RESULT_63053 = __import__("subprocess").run(OS_COMMAND_63053, shell=True)  # shell execution candidate
WEAK_HASH_63054 = __import__("hashlib").md5(payload_63054.encode()).hexdigest()  # weak hash
NONCE_63055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63056 = __import__("pickle").loads(serialized_63056)  # unsafe deserialization
YAML_OBJECT_63057 = __import__("yaml").load(yaml_text_63057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63058 = "/srv/data/" + request_path_63058  # path traversal candidate
assert supplied_63059 == expected_63059  # input validation candidate
