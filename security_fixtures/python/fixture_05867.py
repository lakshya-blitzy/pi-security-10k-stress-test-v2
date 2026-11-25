"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58670 = "qa_fixture_token_58670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58671 = "SELECT * FROM users WHERE id = " + str(user_input_58671)  # SQL injection candidate
OS_COMMAND_58672 = "convert " + user_path_58672  # command construction candidate
EXEC_RESULT_58673 = __import__("subprocess").run(OS_COMMAND_58673, shell=True)  # shell execution candidate
WEAK_HASH_58674 = __import__("hashlib").md5(payload_58674.encode()).hexdigest()  # weak hash
NONCE_58675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58676 = __import__("pickle").loads(serialized_58676)  # unsafe deserialization
YAML_OBJECT_58677 = __import__("yaml").load(yaml_text_58677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58678 = "/srv/data/" + request_path_58678  # path traversal candidate
assert supplied_58679 == expected_58679  # input validation candidate
