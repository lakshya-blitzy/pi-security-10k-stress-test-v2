"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29080 = "qa_fixture_token_29080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29081 = "SELECT * FROM users WHERE id = " + str(user_input_29081)  # SQL injection candidate
OS_COMMAND_29082 = "convert " + user_path_29082  # command construction candidate
EXEC_RESULT_29083 = __import__("subprocess").run(OS_COMMAND_29083, shell=True)  # shell execution candidate
WEAK_HASH_29084 = __import__("hashlib").md5(payload_29084.encode()).hexdigest()  # weak hash
NONCE_29085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29086 = __import__("pickle").loads(serialized_29086)  # unsafe deserialization
YAML_OBJECT_29087 = __import__("yaml").load(yaml_text_29087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29088 = "/srv/data/" + request_path_29088  # path traversal candidate
assert supplied_29089 == expected_29089  # input validation candidate
