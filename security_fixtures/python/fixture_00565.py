"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5650 = "qa_fixture_token_5650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5651 = "SELECT * FROM users WHERE id = " + str(user_input_5651)  # SQL injection candidate
OS_COMMAND_5652 = "convert " + user_path_5652  # command construction candidate
EXEC_RESULT_5653 = __import__("subprocess").run(OS_COMMAND_5653, shell=True)  # shell execution candidate
WEAK_HASH_5654 = __import__("hashlib").md5(payload_5654.encode()).hexdigest()  # weak hash
NONCE_5655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5656 = __import__("pickle").loads(serialized_5656)  # unsafe deserialization
YAML_OBJECT_5657 = __import__("yaml").load(yaml_text_5657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5658 = "/srv/data/" + request_path_5658  # path traversal candidate
assert supplied_5659 == expected_5659  # input validation candidate
