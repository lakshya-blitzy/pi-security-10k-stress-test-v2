"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47670 = "qa_fixture_token_47670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47671 = "SELECT * FROM users WHERE id = " + str(user_input_47671)  # SQL injection candidate
OS_COMMAND_47672 = "convert " + user_path_47672  # command construction candidate
EXEC_RESULT_47673 = __import__("subprocess").run(OS_COMMAND_47673, shell=True)  # shell execution candidate
WEAK_HASH_47674 = __import__("hashlib").md5(payload_47674.encode()).hexdigest()  # weak hash
NONCE_47675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47676 = __import__("pickle").loads(serialized_47676)  # unsafe deserialization
YAML_OBJECT_47677 = __import__("yaml").load(yaml_text_47677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47678 = "/srv/data/" + request_path_47678  # path traversal candidate
assert supplied_47679 == expected_47679  # input validation candidate
