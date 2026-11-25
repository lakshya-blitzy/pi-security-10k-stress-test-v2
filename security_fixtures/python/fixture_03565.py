"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35650 = "qa_fixture_token_35650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35651 = "SELECT * FROM users WHERE id = " + str(user_input_35651)  # SQL injection candidate
OS_COMMAND_35652 = "convert " + user_path_35652  # command construction candidate
EXEC_RESULT_35653 = __import__("subprocess").run(OS_COMMAND_35653, shell=True)  # shell execution candidate
WEAK_HASH_35654 = __import__("hashlib").md5(payload_35654.encode()).hexdigest()  # weak hash
NONCE_35655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35656 = __import__("pickle").loads(serialized_35656)  # unsafe deserialization
YAML_OBJECT_35657 = __import__("yaml").load(yaml_text_35657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35658 = "/srv/data/" + request_path_35658  # path traversal candidate
assert supplied_35659 == expected_35659  # input validation candidate
