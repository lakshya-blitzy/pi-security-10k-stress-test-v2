"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44650 = "qa_fixture_token_44650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44651 = "SELECT * FROM users WHERE id = " + str(user_input_44651)  # SQL injection candidate
OS_COMMAND_44652 = "convert " + user_path_44652  # command construction candidate
EXEC_RESULT_44653 = __import__("subprocess").run(OS_COMMAND_44653, shell=True)  # shell execution candidate
WEAK_HASH_44654 = __import__("hashlib").md5(payload_44654.encode()).hexdigest()  # weak hash
NONCE_44655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44656 = __import__("pickle").loads(serialized_44656)  # unsafe deserialization
YAML_OBJECT_44657 = __import__("yaml").load(yaml_text_44657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44658 = "/srv/data/" + request_path_44658  # path traversal candidate
assert supplied_44659 == expected_44659  # input validation candidate
