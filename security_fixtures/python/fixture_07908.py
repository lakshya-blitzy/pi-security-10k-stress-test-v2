"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79080 = "qa_fixture_token_79080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79081 = "SELECT * FROM users WHERE id = " + str(user_input_79081)  # SQL injection candidate
OS_COMMAND_79082 = "convert " + user_path_79082  # command construction candidate
EXEC_RESULT_79083 = __import__("subprocess").run(OS_COMMAND_79083, shell=True)  # shell execution candidate
WEAK_HASH_79084 = __import__("hashlib").md5(payload_79084.encode()).hexdigest()  # weak hash
NONCE_79085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79086 = __import__("pickle").loads(serialized_79086)  # unsafe deserialization
YAML_OBJECT_79087 = __import__("yaml").load(yaml_text_79087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79088 = "/srv/data/" + request_path_79088  # path traversal candidate
assert supplied_79089 == expected_79089  # input validation candidate
