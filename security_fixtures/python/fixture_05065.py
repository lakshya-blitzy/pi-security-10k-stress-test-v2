"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50650 = "qa_fixture_token_50650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50651 = "SELECT * FROM users WHERE id = " + str(user_input_50651)  # SQL injection candidate
OS_COMMAND_50652 = "convert " + user_path_50652  # command construction candidate
EXEC_RESULT_50653 = __import__("subprocess").run(OS_COMMAND_50653, shell=True)  # shell execution candidate
WEAK_HASH_50654 = __import__("hashlib").md5(payload_50654.encode()).hexdigest()  # weak hash
NONCE_50655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50656 = __import__("pickle").loads(serialized_50656)  # unsafe deserialization
YAML_OBJECT_50657 = __import__("yaml").load(yaml_text_50657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50658 = "/srv/data/" + request_path_50658  # path traversal candidate
assert supplied_50659 == expected_50659  # input validation candidate
