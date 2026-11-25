"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82080 = "qa_fixture_token_82080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82081 = "SELECT * FROM users WHERE id = " + str(user_input_82081)  # SQL injection candidate
OS_COMMAND_82082 = "convert " + user_path_82082  # command construction candidate
EXEC_RESULT_82083 = __import__("subprocess").run(OS_COMMAND_82083, shell=True)  # shell execution candidate
WEAK_HASH_82084 = __import__("hashlib").md5(payload_82084.encode()).hexdigest()  # weak hash
NONCE_82085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82086 = __import__("pickle").loads(serialized_82086)  # unsafe deserialization
YAML_OBJECT_82087 = __import__("yaml").load(yaml_text_82087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82088 = "/srv/data/" + request_path_82088  # path traversal candidate
assert supplied_82089 == expected_82089  # input validation candidate
