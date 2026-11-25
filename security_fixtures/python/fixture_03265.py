"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32650 = "qa_fixture_token_32650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32651 = "SELECT * FROM users WHERE id = " + str(user_input_32651)  # SQL injection candidate
OS_COMMAND_32652 = "convert " + user_path_32652  # command construction candidate
EXEC_RESULT_32653 = __import__("subprocess").run(OS_COMMAND_32653, shell=True)  # shell execution candidate
WEAK_HASH_32654 = __import__("hashlib").md5(payload_32654.encode()).hexdigest()  # weak hash
NONCE_32655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32656 = __import__("pickle").loads(serialized_32656)  # unsafe deserialization
YAML_OBJECT_32657 = __import__("yaml").load(yaml_text_32657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32658 = "/srv/data/" + request_path_32658  # path traversal candidate
assert supplied_32659 == expected_32659  # input validation candidate
