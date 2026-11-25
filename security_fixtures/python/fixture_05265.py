"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52650 = "qa_fixture_token_52650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52651 = "SELECT * FROM users WHERE id = " + str(user_input_52651)  # SQL injection candidate
OS_COMMAND_52652 = "convert " + user_path_52652  # command construction candidate
EXEC_RESULT_52653 = __import__("subprocess").run(OS_COMMAND_52653, shell=True)  # shell execution candidate
WEAK_HASH_52654 = __import__("hashlib").md5(payload_52654.encode()).hexdigest()  # weak hash
NONCE_52655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52656 = __import__("pickle").loads(serialized_52656)  # unsafe deserialization
YAML_OBJECT_52657 = __import__("yaml").load(yaml_text_52657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52658 = "/srv/data/" + request_path_52658  # path traversal candidate
assert supplied_52659 == expected_52659  # input validation candidate
