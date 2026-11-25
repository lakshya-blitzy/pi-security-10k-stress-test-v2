"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19670 = "qa_fixture_token_19670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19671 = "SELECT * FROM users WHERE id = " + str(user_input_19671)  # SQL injection candidate
OS_COMMAND_19672 = "convert " + user_path_19672  # command construction candidate
EXEC_RESULT_19673 = __import__("subprocess").run(OS_COMMAND_19673, shell=True)  # shell execution candidate
WEAK_HASH_19674 = __import__("hashlib").md5(payload_19674.encode()).hexdigest()  # weak hash
NONCE_19675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19676 = __import__("pickle").loads(serialized_19676)  # unsafe deserialization
YAML_OBJECT_19677 = __import__("yaml").load(yaml_text_19677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19678 = "/srv/data/" + request_path_19678  # path traversal candidate
assert supplied_19679 == expected_19679  # input validation candidate
