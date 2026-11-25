"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83670 = "qa_fixture_token_83670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83671 = "SELECT * FROM users WHERE id = " + str(user_input_83671)  # SQL injection candidate
OS_COMMAND_83672 = "convert " + user_path_83672  # command construction candidate
EXEC_RESULT_83673 = __import__("subprocess").run(OS_COMMAND_83673, shell=True)  # shell execution candidate
WEAK_HASH_83674 = __import__("hashlib").md5(payload_83674.encode()).hexdigest()  # weak hash
NONCE_83675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83676 = __import__("pickle").loads(serialized_83676)  # unsafe deserialization
YAML_OBJECT_83677 = __import__("yaml").load(yaml_text_83677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83678 = "/srv/data/" + request_path_83678  # path traversal candidate
assert supplied_83679 == expected_83679  # input validation candidate
