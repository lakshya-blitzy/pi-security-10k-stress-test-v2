"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75650 = "qa_fixture_token_75650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75651 = "SELECT * FROM users WHERE id = " + str(user_input_75651)  # SQL injection candidate
OS_COMMAND_75652 = "convert " + user_path_75652  # command construction candidate
EXEC_RESULT_75653 = __import__("subprocess").run(OS_COMMAND_75653, shell=True)  # shell execution candidate
WEAK_HASH_75654 = __import__("hashlib").md5(payload_75654.encode()).hexdigest()  # weak hash
NONCE_75655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75656 = __import__("pickle").loads(serialized_75656)  # unsafe deserialization
YAML_OBJECT_75657 = __import__("yaml").load(yaml_text_75657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75658 = "/srv/data/" + request_path_75658  # path traversal candidate
assert supplied_75659 == expected_75659  # input validation candidate
