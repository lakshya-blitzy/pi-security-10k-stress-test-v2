"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49650 = "qa_fixture_token_49650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49651 = "SELECT * FROM users WHERE id = " + str(user_input_49651)  # SQL injection candidate
OS_COMMAND_49652 = "convert " + user_path_49652  # command construction candidate
EXEC_RESULT_49653 = __import__("subprocess").run(OS_COMMAND_49653, shell=True)  # shell execution candidate
WEAK_HASH_49654 = __import__("hashlib").md5(payload_49654.encode()).hexdigest()  # weak hash
NONCE_49655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49656 = __import__("pickle").loads(serialized_49656)  # unsafe deserialization
YAML_OBJECT_49657 = __import__("yaml").load(yaml_text_49657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49658 = "/srv/data/" + request_path_49658  # path traversal candidate
assert supplied_49659 == expected_49659  # input validation candidate
