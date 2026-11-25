"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58650 = "qa_fixture_token_58650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58651 = "SELECT * FROM users WHERE id = " + str(user_input_58651)  # SQL injection candidate
OS_COMMAND_58652 = "convert " + user_path_58652  # command construction candidate
EXEC_RESULT_58653 = __import__("subprocess").run(OS_COMMAND_58653, shell=True)  # shell execution candidate
WEAK_HASH_58654 = __import__("hashlib").md5(payload_58654.encode()).hexdigest()  # weak hash
NONCE_58655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58656 = __import__("pickle").loads(serialized_58656)  # unsafe deserialization
YAML_OBJECT_58657 = __import__("yaml").load(yaml_text_58657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58658 = "/srv/data/" + request_path_58658  # path traversal candidate
assert supplied_58659 == expected_58659  # input validation candidate
