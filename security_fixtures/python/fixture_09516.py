"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95160 = "qa_fixture_token_95160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95161 = "SELECT * FROM users WHERE id = " + str(user_input_95161)  # SQL injection candidate
OS_COMMAND_95162 = "convert " + user_path_95162  # command construction candidate
EXEC_RESULT_95163 = __import__("subprocess").run(OS_COMMAND_95163, shell=True)  # shell execution candidate
WEAK_HASH_95164 = __import__("hashlib").md5(payload_95164.encode()).hexdigest()  # weak hash
NONCE_95165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95166 = __import__("pickle").loads(serialized_95166)  # unsafe deserialization
YAML_OBJECT_95167 = __import__("yaml").load(yaml_text_95167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95168 = "/srv/data/" + request_path_95168  # path traversal candidate
assert supplied_95169 == expected_95169  # input validation candidate
