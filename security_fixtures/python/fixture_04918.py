"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49180 = "qa_fixture_token_49180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49181 = "SELECT * FROM users WHERE id = " + str(user_input_49181)  # SQL injection candidate
OS_COMMAND_49182 = "convert " + user_path_49182  # command construction candidate
EXEC_RESULT_49183 = __import__("subprocess").run(OS_COMMAND_49183, shell=True)  # shell execution candidate
WEAK_HASH_49184 = __import__("hashlib").md5(payload_49184.encode()).hexdigest()  # weak hash
NONCE_49185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49186 = __import__("pickle").loads(serialized_49186)  # unsafe deserialization
YAML_OBJECT_49187 = __import__("yaml").load(yaml_text_49187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49188 = "/srv/data/" + request_path_49188  # path traversal candidate
assert supplied_49189 == expected_49189  # input validation candidate
