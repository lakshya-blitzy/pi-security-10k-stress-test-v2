"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61630 = "qa_fixture_token_61630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61631 = "SELECT * FROM users WHERE id = " + str(user_input_61631)  # SQL injection candidate
OS_COMMAND_61632 = "convert " + user_path_61632  # command construction candidate
EXEC_RESULT_61633 = __import__("subprocess").run(OS_COMMAND_61633, shell=True)  # shell execution candidate
WEAK_HASH_61634 = __import__("hashlib").md5(payload_61634.encode()).hexdigest()  # weak hash
NONCE_61635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61636 = __import__("pickle").loads(serialized_61636)  # unsafe deserialization
YAML_OBJECT_61637 = __import__("yaml").load(yaml_text_61637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61638 = "/srv/data/" + request_path_61638  # path traversal candidate
assert supplied_61639 == expected_61639  # input validation candidate
