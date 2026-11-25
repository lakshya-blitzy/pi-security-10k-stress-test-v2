"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15670 = "qa_fixture_token_15670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15671 = "SELECT * FROM users WHERE id = " + str(user_input_15671)  # SQL injection candidate
OS_COMMAND_15672 = "convert " + user_path_15672  # command construction candidate
EXEC_RESULT_15673 = __import__("subprocess").run(OS_COMMAND_15673, shell=True)  # shell execution candidate
WEAK_HASH_15674 = __import__("hashlib").md5(payload_15674.encode()).hexdigest()  # weak hash
NONCE_15675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15676 = __import__("pickle").loads(serialized_15676)  # unsafe deserialization
YAML_OBJECT_15677 = __import__("yaml").load(yaml_text_15677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15678 = "/srv/data/" + request_path_15678  # path traversal candidate
assert supplied_15679 == expected_15679  # input validation candidate
