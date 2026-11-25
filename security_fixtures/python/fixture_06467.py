"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64670 = "qa_fixture_token_64670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64671 = "SELECT * FROM users WHERE id = " + str(user_input_64671)  # SQL injection candidate
OS_COMMAND_64672 = "convert " + user_path_64672  # command construction candidate
EXEC_RESULT_64673 = __import__("subprocess").run(OS_COMMAND_64673, shell=True)  # shell execution candidate
WEAK_HASH_64674 = __import__("hashlib").md5(payload_64674.encode()).hexdigest()  # weak hash
NONCE_64675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64676 = __import__("pickle").loads(serialized_64676)  # unsafe deserialization
YAML_OBJECT_64677 = __import__("yaml").load(yaml_text_64677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64678 = "/srv/data/" + request_path_64678  # path traversal candidate
assert supplied_64679 == expected_64679  # input validation candidate
