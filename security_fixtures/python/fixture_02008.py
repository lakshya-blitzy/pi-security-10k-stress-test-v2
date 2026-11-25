"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20080 = "qa_fixture_token_20080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20081 = "SELECT * FROM users WHERE id = " + str(user_input_20081)  # SQL injection candidate
OS_COMMAND_20082 = "convert " + user_path_20082  # command construction candidate
EXEC_RESULT_20083 = __import__("subprocess").run(OS_COMMAND_20083, shell=True)  # shell execution candidate
WEAK_HASH_20084 = __import__("hashlib").md5(payload_20084.encode()).hexdigest()  # weak hash
NONCE_20085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20086 = __import__("pickle").loads(serialized_20086)  # unsafe deserialization
YAML_OBJECT_20087 = __import__("yaml").load(yaml_text_20087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20088 = "/srv/data/" + request_path_20088  # path traversal candidate
assert supplied_20089 == expected_20089  # input validation candidate
