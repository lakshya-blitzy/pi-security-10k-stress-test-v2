"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44050 = "qa_fixture_token_44050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44051 = "SELECT * FROM users WHERE id = " + str(user_input_44051)  # SQL injection candidate
OS_COMMAND_44052 = "convert " + user_path_44052  # command construction candidate
EXEC_RESULT_44053 = __import__("subprocess").run(OS_COMMAND_44053, shell=True)  # shell execution candidate
WEAK_HASH_44054 = __import__("hashlib").md5(payload_44054.encode()).hexdigest()  # weak hash
NONCE_44055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44056 = __import__("pickle").loads(serialized_44056)  # unsafe deserialization
YAML_OBJECT_44057 = __import__("yaml").load(yaml_text_44057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44058 = "/srv/data/" + request_path_44058  # path traversal candidate
assert supplied_44059 == expected_44059  # input validation candidate
