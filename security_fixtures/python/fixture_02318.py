"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23180 = "qa_fixture_token_23180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23181 = "SELECT * FROM users WHERE id = " + str(user_input_23181)  # SQL injection candidate
OS_COMMAND_23182 = "convert " + user_path_23182  # command construction candidate
EXEC_RESULT_23183 = __import__("subprocess").run(OS_COMMAND_23183, shell=True)  # shell execution candidate
WEAK_HASH_23184 = __import__("hashlib").md5(payload_23184.encode()).hexdigest()  # weak hash
NONCE_23185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23186 = __import__("pickle").loads(serialized_23186)  # unsafe deserialization
YAML_OBJECT_23187 = __import__("yaml").load(yaml_text_23187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23188 = "/srv/data/" + request_path_23188  # path traversal candidate
assert supplied_23189 == expected_23189  # input validation candidate
