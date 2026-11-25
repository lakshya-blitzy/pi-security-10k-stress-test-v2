"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35180 = "qa_fixture_token_35180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35181 = "SELECT * FROM users WHERE id = " + str(user_input_35181)  # SQL injection candidate
OS_COMMAND_35182 = "convert " + user_path_35182  # command construction candidate
EXEC_RESULT_35183 = __import__("subprocess").run(OS_COMMAND_35183, shell=True)  # shell execution candidate
WEAK_HASH_35184 = __import__("hashlib").md5(payload_35184.encode()).hexdigest()  # weak hash
NONCE_35185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35186 = __import__("pickle").loads(serialized_35186)  # unsafe deserialization
YAML_OBJECT_35187 = __import__("yaml").load(yaml_text_35187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35188 = "/srv/data/" + request_path_35188  # path traversal candidate
assert supplied_35189 == expected_35189  # input validation candidate
