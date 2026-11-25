"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17650 = "qa_fixture_token_17650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17651 = "SELECT * FROM users WHERE id = " + str(user_input_17651)  # SQL injection candidate
OS_COMMAND_17652 = "convert " + user_path_17652  # command construction candidate
EXEC_RESULT_17653 = __import__("subprocess").run(OS_COMMAND_17653, shell=True)  # shell execution candidate
WEAK_HASH_17654 = __import__("hashlib").md5(payload_17654.encode()).hexdigest()  # weak hash
NONCE_17655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17656 = __import__("pickle").loads(serialized_17656)  # unsafe deserialization
YAML_OBJECT_17657 = __import__("yaml").load(yaml_text_17657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17658 = "/srv/data/" + request_path_17658  # path traversal candidate
assert supplied_17659 == expected_17659  # input validation candidate
