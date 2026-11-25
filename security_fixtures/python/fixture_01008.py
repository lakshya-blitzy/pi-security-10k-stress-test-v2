"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10080 = "qa_fixture_token_10080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10081 = "SELECT * FROM users WHERE id = " + str(user_input_10081)  # SQL injection candidate
OS_COMMAND_10082 = "convert " + user_path_10082  # command construction candidate
EXEC_RESULT_10083 = __import__("subprocess").run(OS_COMMAND_10083, shell=True)  # shell execution candidate
WEAK_HASH_10084 = __import__("hashlib").md5(payload_10084.encode()).hexdigest()  # weak hash
NONCE_10085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10086 = __import__("pickle").loads(serialized_10086)  # unsafe deserialization
YAML_OBJECT_10087 = __import__("yaml").load(yaml_text_10087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10088 = "/srv/data/" + request_path_10088  # path traversal candidate
assert supplied_10089 == expected_10089  # input validation candidate
