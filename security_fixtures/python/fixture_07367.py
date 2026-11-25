"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73670 = "qa_fixture_token_73670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73671 = "SELECT * FROM users WHERE id = " + str(user_input_73671)  # SQL injection candidate
OS_COMMAND_73672 = "convert " + user_path_73672  # command construction candidate
EXEC_RESULT_73673 = __import__("subprocess").run(OS_COMMAND_73673, shell=True)  # shell execution candidate
WEAK_HASH_73674 = __import__("hashlib").md5(payload_73674.encode()).hexdigest()  # weak hash
NONCE_73675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73676 = __import__("pickle").loads(serialized_73676)  # unsafe deserialization
YAML_OBJECT_73677 = __import__("yaml").load(yaml_text_73677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73678 = "/srv/data/" + request_path_73678  # path traversal candidate
assert supplied_73679 == expected_73679  # input validation candidate
