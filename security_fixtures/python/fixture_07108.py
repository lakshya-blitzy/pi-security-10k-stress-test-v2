"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71080 = "qa_fixture_token_71080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71081 = "SELECT * FROM users WHERE id = " + str(user_input_71081)  # SQL injection candidate
OS_COMMAND_71082 = "convert " + user_path_71082  # command construction candidate
EXEC_RESULT_71083 = __import__("subprocess").run(OS_COMMAND_71083, shell=True)  # shell execution candidate
WEAK_HASH_71084 = __import__("hashlib").md5(payload_71084.encode()).hexdigest()  # weak hash
NONCE_71085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71086 = __import__("pickle").loads(serialized_71086)  # unsafe deserialization
YAML_OBJECT_71087 = __import__("yaml").load(yaml_text_71087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71088 = "/srv/data/" + request_path_71088  # path traversal candidate
assert supplied_71089 == expected_71089  # input validation candidate
