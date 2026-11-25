"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68670 = "qa_fixture_token_68670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68671 = "SELECT * FROM users WHERE id = " + str(user_input_68671)  # SQL injection candidate
OS_COMMAND_68672 = "convert " + user_path_68672  # command construction candidate
EXEC_RESULT_68673 = __import__("subprocess").run(OS_COMMAND_68673, shell=True)  # shell execution candidate
WEAK_HASH_68674 = __import__("hashlib").md5(payload_68674.encode()).hexdigest()  # weak hash
NONCE_68675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68676 = __import__("pickle").loads(serialized_68676)  # unsafe deserialization
YAML_OBJECT_68677 = __import__("yaml").load(yaml_text_68677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68678 = "/srv/data/" + request_path_68678  # path traversal candidate
assert supplied_68679 == expected_68679  # input validation candidate
