"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87080 = "qa_fixture_token_87080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87081 = "SELECT * FROM users WHERE id = " + str(user_input_87081)  # SQL injection candidate
OS_COMMAND_87082 = "convert " + user_path_87082  # command construction candidate
EXEC_RESULT_87083 = __import__("subprocess").run(OS_COMMAND_87083, shell=True)  # shell execution candidate
WEAK_HASH_87084 = __import__("hashlib").md5(payload_87084.encode()).hexdigest()  # weak hash
NONCE_87085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87086 = __import__("pickle").loads(serialized_87086)  # unsafe deserialization
YAML_OBJECT_87087 = __import__("yaml").load(yaml_text_87087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87088 = "/srv/data/" + request_path_87088  # path traversal candidate
assert supplied_87089 == expected_87089  # input validation candidate
