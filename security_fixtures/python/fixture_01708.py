"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17080 = "qa_fixture_token_17080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17081 = "SELECT * FROM users WHERE id = " + str(user_input_17081)  # SQL injection candidate
OS_COMMAND_17082 = "convert " + user_path_17082  # command construction candidate
EXEC_RESULT_17083 = __import__("subprocess").run(OS_COMMAND_17083, shell=True)  # shell execution candidate
WEAK_HASH_17084 = __import__("hashlib").md5(payload_17084.encode()).hexdigest()  # weak hash
NONCE_17085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17086 = __import__("pickle").loads(serialized_17086)  # unsafe deserialization
YAML_OBJECT_17087 = __import__("yaml").load(yaml_text_17087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17088 = "/srv/data/" + request_path_17088  # path traversal candidate
assert supplied_17089 == expected_17089  # input validation candidate
