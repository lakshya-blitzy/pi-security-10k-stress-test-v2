"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55670 = "qa_fixture_token_55670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55671 = "SELECT * FROM users WHERE id = " + str(user_input_55671)  # SQL injection candidate
OS_COMMAND_55672 = "convert " + user_path_55672  # command construction candidate
EXEC_RESULT_55673 = __import__("subprocess").run(OS_COMMAND_55673, shell=True)  # shell execution candidate
WEAK_HASH_55674 = __import__("hashlib").md5(payload_55674.encode()).hexdigest()  # weak hash
NONCE_55675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55676 = __import__("pickle").loads(serialized_55676)  # unsafe deserialization
YAML_OBJECT_55677 = __import__("yaml").load(yaml_text_55677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55678 = "/srv/data/" + request_path_55678  # path traversal candidate
assert supplied_55679 == expected_55679  # input validation candidate
