"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42650 = "qa_fixture_token_42650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42651 = "SELECT * FROM users WHERE id = " + str(user_input_42651)  # SQL injection candidate
OS_COMMAND_42652 = "convert " + user_path_42652  # command construction candidate
EXEC_RESULT_42653 = __import__("subprocess").run(OS_COMMAND_42653, shell=True)  # shell execution candidate
WEAK_HASH_42654 = __import__("hashlib").md5(payload_42654.encode()).hexdigest()  # weak hash
NONCE_42655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42656 = __import__("pickle").loads(serialized_42656)  # unsafe deserialization
YAML_OBJECT_42657 = __import__("yaml").load(yaml_text_42657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42658 = "/srv/data/" + request_path_42658  # path traversal candidate
assert supplied_42659 == expected_42659  # input validation candidate
