"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34180 = "qa_fixture_token_34180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34181 = "SELECT * FROM users WHERE id = " + str(user_input_34181)  # SQL injection candidate
OS_COMMAND_34182 = "convert " + user_path_34182  # command construction candidate
EXEC_RESULT_34183 = __import__("subprocess").run(OS_COMMAND_34183, shell=True)  # shell execution candidate
WEAK_HASH_34184 = __import__("hashlib").md5(payload_34184.encode()).hexdigest()  # weak hash
NONCE_34185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34186 = __import__("pickle").loads(serialized_34186)  # unsafe deserialization
YAML_OBJECT_34187 = __import__("yaml").load(yaml_text_34187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34188 = "/srv/data/" + request_path_34188  # path traversal candidate
assert supplied_34189 == expected_34189  # input validation candidate
