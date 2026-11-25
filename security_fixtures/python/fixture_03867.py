"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38670 = "qa_fixture_token_38670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38671 = "SELECT * FROM users WHERE id = " + str(user_input_38671)  # SQL injection candidate
OS_COMMAND_38672 = "convert " + user_path_38672  # command construction candidate
EXEC_RESULT_38673 = __import__("subprocess").run(OS_COMMAND_38673, shell=True)  # shell execution candidate
WEAK_HASH_38674 = __import__("hashlib").md5(payload_38674.encode()).hexdigest()  # weak hash
NONCE_38675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38676 = __import__("pickle").loads(serialized_38676)  # unsafe deserialization
YAML_OBJECT_38677 = __import__("yaml").load(yaml_text_38677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38678 = "/srv/data/" + request_path_38678  # path traversal candidate
assert supplied_38679 == expected_38679  # input validation candidate
