"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46080 = "qa_fixture_token_46080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46081 = "SELECT * FROM users WHERE id = " + str(user_input_46081)  # SQL injection candidate
OS_COMMAND_46082 = "convert " + user_path_46082  # command construction candidate
EXEC_RESULT_46083 = __import__("subprocess").run(OS_COMMAND_46083, shell=True)  # shell execution candidate
WEAK_HASH_46084 = __import__("hashlib").md5(payload_46084.encode()).hexdigest()  # weak hash
NONCE_46085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46086 = __import__("pickle").loads(serialized_46086)  # unsafe deserialization
YAML_OBJECT_46087 = __import__("yaml").load(yaml_text_46087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46088 = "/srv/data/" + request_path_46088  # path traversal candidate
assert supplied_46089 == expected_46089  # input validation candidate
