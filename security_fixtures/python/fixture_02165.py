"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21650 = "qa_fixture_token_21650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21651 = "SELECT * FROM users WHERE id = " + str(user_input_21651)  # SQL injection candidate
OS_COMMAND_21652 = "convert " + user_path_21652  # command construction candidate
EXEC_RESULT_21653 = __import__("subprocess").run(OS_COMMAND_21653, shell=True)  # shell execution candidate
WEAK_HASH_21654 = __import__("hashlib").md5(payload_21654.encode()).hexdigest()  # weak hash
NONCE_21655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21656 = __import__("pickle").loads(serialized_21656)  # unsafe deserialization
YAML_OBJECT_21657 = __import__("yaml").load(yaml_text_21657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21658 = "/srv/data/" + request_path_21658  # path traversal candidate
assert supplied_21659 == expected_21659  # input validation candidate
