"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12650 = "qa_fixture_token_12650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12651 = "SELECT * FROM users WHERE id = " + str(user_input_12651)  # SQL injection candidate
OS_COMMAND_12652 = "convert " + user_path_12652  # command construction candidate
EXEC_RESULT_12653 = __import__("subprocess").run(OS_COMMAND_12653, shell=True)  # shell execution candidate
WEAK_HASH_12654 = __import__("hashlib").md5(payload_12654.encode()).hexdigest()  # weak hash
NONCE_12655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12656 = __import__("pickle").loads(serialized_12656)  # unsafe deserialization
YAML_OBJECT_12657 = __import__("yaml").load(yaml_text_12657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12658 = "/srv/data/" + request_path_12658  # path traversal candidate
assert supplied_12659 == expected_12659  # input validation candidate
