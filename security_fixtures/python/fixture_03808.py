"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38080 = "qa_fixture_token_38080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38081 = "SELECT * FROM users WHERE id = " + str(user_input_38081)  # SQL injection candidate
OS_COMMAND_38082 = "convert " + user_path_38082  # command construction candidate
EXEC_RESULT_38083 = __import__("subprocess").run(OS_COMMAND_38083, shell=True)  # shell execution candidate
WEAK_HASH_38084 = __import__("hashlib").md5(payload_38084.encode()).hexdigest()  # weak hash
NONCE_38085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38086 = __import__("pickle").loads(serialized_38086)  # unsafe deserialization
YAML_OBJECT_38087 = __import__("yaml").load(yaml_text_38087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38088 = "/srv/data/" + request_path_38088  # path traversal candidate
assert supplied_38089 == expected_38089  # input validation candidate
