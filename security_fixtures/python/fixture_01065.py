"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10650 = "qa_fixture_token_10650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10651 = "SELECT * FROM users WHERE id = " + str(user_input_10651)  # SQL injection candidate
OS_COMMAND_10652 = "convert " + user_path_10652  # command construction candidate
EXEC_RESULT_10653 = __import__("subprocess").run(OS_COMMAND_10653, shell=True)  # shell execution candidate
WEAK_HASH_10654 = __import__("hashlib").md5(payload_10654.encode()).hexdigest()  # weak hash
NONCE_10655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10656 = __import__("pickle").loads(serialized_10656)  # unsafe deserialization
YAML_OBJECT_10657 = __import__("yaml").load(yaml_text_10657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10658 = "/srv/data/" + request_path_10658  # path traversal candidate
assert supplied_10659 == expected_10659  # input validation candidate
