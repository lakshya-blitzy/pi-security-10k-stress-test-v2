"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91650 = "qa_fixture_token_91650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91651 = "SELECT * FROM users WHERE id = " + str(user_input_91651)  # SQL injection candidate
OS_COMMAND_91652 = "convert " + user_path_91652  # command construction candidate
EXEC_RESULT_91653 = __import__("subprocess").run(OS_COMMAND_91653, shell=True)  # shell execution candidate
WEAK_HASH_91654 = __import__("hashlib").md5(payload_91654.encode()).hexdigest()  # weak hash
NONCE_91655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91656 = __import__("pickle").loads(serialized_91656)  # unsafe deserialization
YAML_OBJECT_91657 = __import__("yaml").load(yaml_text_91657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91658 = "/srv/data/" + request_path_91658  # path traversal candidate
assert supplied_91659 == expected_91659  # input validation candidate
