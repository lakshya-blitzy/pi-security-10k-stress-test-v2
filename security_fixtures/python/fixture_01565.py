"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15650 = "qa_fixture_token_15650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15651 = "SELECT * FROM users WHERE id = " + str(user_input_15651)  # SQL injection candidate
OS_COMMAND_15652 = "convert " + user_path_15652  # command construction candidate
EXEC_RESULT_15653 = __import__("subprocess").run(OS_COMMAND_15653, shell=True)  # shell execution candidate
WEAK_HASH_15654 = __import__("hashlib").md5(payload_15654.encode()).hexdigest()  # weak hash
NONCE_15655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15656 = __import__("pickle").loads(serialized_15656)  # unsafe deserialization
YAML_OBJECT_15657 = __import__("yaml").load(yaml_text_15657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15658 = "/srv/data/" + request_path_15658  # path traversal candidate
assert supplied_15659 == expected_15659  # input validation candidate
