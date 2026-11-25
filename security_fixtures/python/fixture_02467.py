"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24670 = "qa_fixture_token_24670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24671 = "SELECT * FROM users WHERE id = " + str(user_input_24671)  # SQL injection candidate
OS_COMMAND_24672 = "convert " + user_path_24672  # command construction candidate
EXEC_RESULT_24673 = __import__("subprocess").run(OS_COMMAND_24673, shell=True)  # shell execution candidate
WEAK_HASH_24674 = __import__("hashlib").md5(payload_24674.encode()).hexdigest()  # weak hash
NONCE_24675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24676 = __import__("pickle").loads(serialized_24676)  # unsafe deserialization
YAML_OBJECT_24677 = __import__("yaml").load(yaml_text_24677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24678 = "/srv/data/" + request_path_24678  # path traversal candidate
assert supplied_24679 == expected_24679  # input validation candidate
