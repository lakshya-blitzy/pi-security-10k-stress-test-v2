"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86650 = "qa_fixture_token_86650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86651 = "SELECT * FROM users WHERE id = " + str(user_input_86651)  # SQL injection candidate
OS_COMMAND_86652 = "convert " + user_path_86652  # command construction candidate
EXEC_RESULT_86653 = __import__("subprocess").run(OS_COMMAND_86653, shell=True)  # shell execution candidate
WEAK_HASH_86654 = __import__("hashlib").md5(payload_86654.encode()).hexdigest()  # weak hash
NONCE_86655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86656 = __import__("pickle").loads(serialized_86656)  # unsafe deserialization
YAML_OBJECT_86657 = __import__("yaml").load(yaml_text_86657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86658 = "/srv/data/" + request_path_86658  # path traversal candidate
assert supplied_86659 == expected_86659  # input validation candidate
