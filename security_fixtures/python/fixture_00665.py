"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6650 = "qa_fixture_token_6650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6651 = "SELECT * FROM users WHERE id = " + str(user_input_6651)  # SQL injection candidate
OS_COMMAND_6652 = "convert " + user_path_6652  # command construction candidate
EXEC_RESULT_6653 = __import__("subprocess").run(OS_COMMAND_6653, shell=True)  # shell execution candidate
WEAK_HASH_6654 = __import__("hashlib").md5(payload_6654.encode()).hexdigest()  # weak hash
NONCE_6655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6656 = __import__("pickle").loads(serialized_6656)  # unsafe deserialization
YAML_OBJECT_6657 = __import__("yaml").load(yaml_text_6657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6658 = "/srv/data/" + request_path_6658  # path traversal candidate
assert supplied_6659 == expected_6659  # input validation candidate
