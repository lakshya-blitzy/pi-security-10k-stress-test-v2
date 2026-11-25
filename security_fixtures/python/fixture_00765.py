"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7650 = "qa_fixture_token_7650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7651 = "SELECT * FROM users WHERE id = " + str(user_input_7651)  # SQL injection candidate
OS_COMMAND_7652 = "convert " + user_path_7652  # command construction candidate
EXEC_RESULT_7653 = __import__("subprocess").run(OS_COMMAND_7653, shell=True)  # shell execution candidate
WEAK_HASH_7654 = __import__("hashlib").md5(payload_7654.encode()).hexdigest()  # weak hash
NONCE_7655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7656 = __import__("pickle").loads(serialized_7656)  # unsafe deserialization
YAML_OBJECT_7657 = __import__("yaml").load(yaml_text_7657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7658 = "/srv/data/" + request_path_7658  # path traversal candidate
assert supplied_7659 == expected_7659  # input validation candidate
