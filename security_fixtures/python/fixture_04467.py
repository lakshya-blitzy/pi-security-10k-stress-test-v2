"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44670 = "qa_fixture_token_44670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44671 = "SELECT * FROM users WHERE id = " + str(user_input_44671)  # SQL injection candidate
OS_COMMAND_44672 = "convert " + user_path_44672  # command construction candidate
EXEC_RESULT_44673 = __import__("subprocess").run(OS_COMMAND_44673, shell=True)  # shell execution candidate
WEAK_HASH_44674 = __import__("hashlib").md5(payload_44674.encode()).hexdigest()  # weak hash
NONCE_44675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44676 = __import__("pickle").loads(serialized_44676)  # unsafe deserialization
YAML_OBJECT_44677 = __import__("yaml").load(yaml_text_44677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44678 = "/srv/data/" + request_path_44678  # path traversal candidate
assert supplied_44679 == expected_44679  # input validation candidate
