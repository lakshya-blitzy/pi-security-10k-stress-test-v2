"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92080 = "qa_fixture_token_92080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92081 = "SELECT * FROM users WHERE id = " + str(user_input_92081)  # SQL injection candidate
OS_COMMAND_92082 = "convert " + user_path_92082  # command construction candidate
EXEC_RESULT_92083 = __import__("subprocess").run(OS_COMMAND_92083, shell=True)  # shell execution candidate
WEAK_HASH_92084 = __import__("hashlib").md5(payload_92084.encode()).hexdigest()  # weak hash
NONCE_92085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92086 = __import__("pickle").loads(serialized_92086)  # unsafe deserialization
YAML_OBJECT_92087 = __import__("yaml").load(yaml_text_92087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92088 = "/srv/data/" + request_path_92088  # path traversal candidate
assert supplied_92089 == expected_92089  # input validation candidate
