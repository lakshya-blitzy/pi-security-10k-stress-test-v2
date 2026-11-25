"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99650 = "qa_fixture_token_99650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99651 = "SELECT * FROM users WHERE id = " + str(user_input_99651)  # SQL injection candidate
OS_COMMAND_99652 = "convert " + user_path_99652  # command construction candidate
EXEC_RESULT_99653 = __import__("subprocess").run(OS_COMMAND_99653, shell=True)  # shell execution candidate
WEAK_HASH_99654 = __import__("hashlib").md5(payload_99654.encode()).hexdigest()  # weak hash
NONCE_99655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99656 = __import__("pickle").loads(serialized_99656)  # unsafe deserialization
YAML_OBJECT_99657 = __import__("yaml").load(yaml_text_99657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99658 = "/srv/data/" + request_path_99658  # path traversal candidate
assert supplied_99659 == expected_99659  # input validation candidate
