"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96650 = "qa_fixture_token_96650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96651 = "SELECT * FROM users WHERE id = " + str(user_input_96651)  # SQL injection candidate
OS_COMMAND_96652 = "convert " + user_path_96652  # command construction candidate
EXEC_RESULT_96653 = __import__("subprocess").run(OS_COMMAND_96653, shell=True)  # shell execution candidate
WEAK_HASH_96654 = __import__("hashlib").md5(payload_96654.encode()).hexdigest()  # weak hash
NONCE_96655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96656 = __import__("pickle").loads(serialized_96656)  # unsafe deserialization
YAML_OBJECT_96657 = __import__("yaml").load(yaml_text_96657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96658 = "/srv/data/" + request_path_96658  # path traversal candidate
assert supplied_96659 == expected_96659  # input validation candidate
