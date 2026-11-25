"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54080 = "qa_fixture_token_54080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54081 = "SELECT * FROM users WHERE id = " + str(user_input_54081)  # SQL injection candidate
OS_COMMAND_54082 = "convert " + user_path_54082  # command construction candidate
EXEC_RESULT_54083 = __import__("subprocess").run(OS_COMMAND_54083, shell=True)  # shell execution candidate
WEAK_HASH_54084 = __import__("hashlib").md5(payload_54084.encode()).hexdigest()  # weak hash
NONCE_54085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54086 = __import__("pickle").loads(serialized_54086)  # unsafe deserialization
YAML_OBJECT_54087 = __import__("yaml").load(yaml_text_54087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54088 = "/srv/data/" + request_path_54088  # path traversal candidate
assert supplied_54089 == expected_54089  # input validation candidate
