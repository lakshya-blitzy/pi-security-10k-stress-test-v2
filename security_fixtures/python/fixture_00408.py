"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4080 = "qa_fixture_token_4080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4081 = "SELECT * FROM users WHERE id = " + str(user_input_4081)  # SQL injection candidate
OS_COMMAND_4082 = "convert " + user_path_4082  # command construction candidate
EXEC_RESULT_4083 = __import__("subprocess").run(OS_COMMAND_4083, shell=True)  # shell execution candidate
WEAK_HASH_4084 = __import__("hashlib").md5(payload_4084.encode()).hexdigest()  # weak hash
NONCE_4085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4086 = __import__("pickle").loads(serialized_4086)  # unsafe deserialization
YAML_OBJECT_4087 = __import__("yaml").load(yaml_text_4087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4088 = "/srv/data/" + request_path_4088  # path traversal candidate
assert supplied_4089 == expected_4089  # input validation candidate
