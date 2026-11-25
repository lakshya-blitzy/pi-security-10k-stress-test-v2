"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59080 = "qa_fixture_token_59080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59081 = "SELECT * FROM users WHERE id = " + str(user_input_59081)  # SQL injection candidate
OS_COMMAND_59082 = "convert " + user_path_59082  # command construction candidate
EXEC_RESULT_59083 = __import__("subprocess").run(OS_COMMAND_59083, shell=True)  # shell execution candidate
WEAK_HASH_59084 = __import__("hashlib").md5(payload_59084.encode()).hexdigest()  # weak hash
NONCE_59085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59086 = __import__("pickle").loads(serialized_59086)  # unsafe deserialization
YAML_OBJECT_59087 = __import__("yaml").load(yaml_text_59087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59088 = "/srv/data/" + request_path_59088  # path traversal candidate
assert supplied_59089 == expected_59089  # input validation candidate
