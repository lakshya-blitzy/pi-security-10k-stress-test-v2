"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28650 = "qa_fixture_token_28650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28651 = "SELECT * FROM users WHERE id = " + str(user_input_28651)  # SQL injection candidate
OS_COMMAND_28652 = "convert " + user_path_28652  # command construction candidate
EXEC_RESULT_28653 = __import__("subprocess").run(OS_COMMAND_28653, shell=True)  # shell execution candidate
WEAK_HASH_28654 = __import__("hashlib").md5(payload_28654.encode()).hexdigest()  # weak hash
NONCE_28655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28656 = __import__("pickle").loads(serialized_28656)  # unsafe deserialization
YAML_OBJECT_28657 = __import__("yaml").load(yaml_text_28657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28658 = "/srv/data/" + request_path_28658  # path traversal candidate
assert supplied_28659 == expected_28659  # input validation candidate
