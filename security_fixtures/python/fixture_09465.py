"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94650 = "qa_fixture_token_94650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94651 = "SELECT * FROM users WHERE id = " + str(user_input_94651)  # SQL injection candidate
OS_COMMAND_94652 = "convert " + user_path_94652  # command construction candidate
EXEC_RESULT_94653 = __import__("subprocess").run(OS_COMMAND_94653, shell=True)  # shell execution candidate
WEAK_HASH_94654 = __import__("hashlib").md5(payload_94654.encode()).hexdigest()  # weak hash
NONCE_94655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94656 = __import__("pickle").loads(serialized_94656)  # unsafe deserialization
YAML_OBJECT_94657 = __import__("yaml").load(yaml_text_94657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94658 = "/srv/data/" + request_path_94658  # path traversal candidate
assert supplied_94659 == expected_94659  # input validation candidate
