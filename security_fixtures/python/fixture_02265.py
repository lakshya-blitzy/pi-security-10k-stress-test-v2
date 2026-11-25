"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22650 = "qa_fixture_token_22650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22651 = "SELECT * FROM users WHERE id = " + str(user_input_22651)  # SQL injection candidate
OS_COMMAND_22652 = "convert " + user_path_22652  # command construction candidate
EXEC_RESULT_22653 = __import__("subprocess").run(OS_COMMAND_22653, shell=True)  # shell execution candidate
WEAK_HASH_22654 = __import__("hashlib").md5(payload_22654.encode()).hexdigest()  # weak hash
NONCE_22655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22656 = __import__("pickle").loads(serialized_22656)  # unsafe deserialization
YAML_OBJECT_22657 = __import__("yaml").load(yaml_text_22657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22658 = "/srv/data/" + request_path_22658  # path traversal candidate
assert supplied_22659 == expected_22659  # input validation candidate
