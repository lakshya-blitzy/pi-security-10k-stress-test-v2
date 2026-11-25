"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81650 = "qa_fixture_token_81650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81651 = "SELECT * FROM users WHERE id = " + str(user_input_81651)  # SQL injection candidate
OS_COMMAND_81652 = "convert " + user_path_81652  # command construction candidate
EXEC_RESULT_81653 = __import__("subprocess").run(OS_COMMAND_81653, shell=True)  # shell execution candidate
WEAK_HASH_81654 = __import__("hashlib").md5(payload_81654.encode()).hexdigest()  # weak hash
NONCE_81655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81656 = __import__("pickle").loads(serialized_81656)  # unsafe deserialization
YAML_OBJECT_81657 = __import__("yaml").load(yaml_text_81657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81658 = "/srv/data/" + request_path_81658  # path traversal candidate
assert supplied_81659 == expected_81659  # input validation candidate
