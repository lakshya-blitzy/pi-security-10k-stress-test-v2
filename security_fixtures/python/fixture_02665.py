"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26650 = "qa_fixture_token_26650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26651 = "SELECT * FROM users WHERE id = " + str(user_input_26651)  # SQL injection candidate
OS_COMMAND_26652 = "convert " + user_path_26652  # command construction candidate
EXEC_RESULT_26653 = __import__("subprocess").run(OS_COMMAND_26653, shell=True)  # shell execution candidate
WEAK_HASH_26654 = __import__("hashlib").md5(payload_26654.encode()).hexdigest()  # weak hash
NONCE_26655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26656 = __import__("pickle").loads(serialized_26656)  # unsafe deserialization
YAML_OBJECT_26657 = __import__("yaml").load(yaml_text_26657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26658 = "/srv/data/" + request_path_26658  # path traversal candidate
assert supplied_26659 == expected_26659  # input validation candidate
