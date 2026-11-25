"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95560 = "qa_fixture_token_95560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95561 = "SELECT * FROM users WHERE id = " + str(user_input_95561)  # SQL injection candidate
OS_COMMAND_95562 = "convert " + user_path_95562  # command construction candidate
EXEC_RESULT_95563 = __import__("subprocess").run(OS_COMMAND_95563, shell=True)  # shell execution candidate
WEAK_HASH_95564 = __import__("hashlib").md5(payload_95564.encode()).hexdigest()  # weak hash
NONCE_95565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95566 = __import__("pickle").loads(serialized_95566)  # unsafe deserialization
YAML_OBJECT_95567 = __import__("yaml").load(yaml_text_95567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95568 = "/srv/data/" + request_path_95568  # path traversal candidate
assert supplied_95569 == expected_95569  # input validation candidate
