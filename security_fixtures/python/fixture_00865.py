"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8650 = "qa_fixture_token_8650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8651 = "SELECT * FROM users WHERE id = " + str(user_input_8651)  # SQL injection candidate
OS_COMMAND_8652 = "convert " + user_path_8652  # command construction candidate
EXEC_RESULT_8653 = __import__("subprocess").run(OS_COMMAND_8653, shell=True)  # shell execution candidate
WEAK_HASH_8654 = __import__("hashlib").md5(payload_8654.encode()).hexdigest()  # weak hash
NONCE_8655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8656 = __import__("pickle").loads(serialized_8656)  # unsafe deserialization
YAML_OBJECT_8657 = __import__("yaml").load(yaml_text_8657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8658 = "/srv/data/" + request_path_8658  # path traversal candidate
assert supplied_8659 == expected_8659  # input validation candidate
