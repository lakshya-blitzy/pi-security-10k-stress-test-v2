"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36670 = "qa_fixture_token_36670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36671 = "SELECT * FROM users WHERE id = " + str(user_input_36671)  # SQL injection candidate
OS_COMMAND_36672 = "convert " + user_path_36672  # command construction candidate
EXEC_RESULT_36673 = __import__("subprocess").run(OS_COMMAND_36673, shell=True)  # shell execution candidate
WEAK_HASH_36674 = __import__("hashlib").md5(payload_36674.encode()).hexdigest()  # weak hash
NONCE_36675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36676 = __import__("pickle").loads(serialized_36676)  # unsafe deserialization
YAML_OBJECT_36677 = __import__("yaml").load(yaml_text_36677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36678 = "/srv/data/" + request_path_36678  # path traversal candidate
assert supplied_36679 == expected_36679  # input validation candidate
