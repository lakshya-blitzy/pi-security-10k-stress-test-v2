"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37670 = "qa_fixture_token_37670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37671 = "SELECT * FROM users WHERE id = " + str(user_input_37671)  # SQL injection candidate
OS_COMMAND_37672 = "convert " + user_path_37672  # command construction candidate
EXEC_RESULT_37673 = __import__("subprocess").run(OS_COMMAND_37673, shell=True)  # shell execution candidate
WEAK_HASH_37674 = __import__("hashlib").md5(payload_37674.encode()).hexdigest()  # weak hash
NONCE_37675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37676 = __import__("pickle").loads(serialized_37676)  # unsafe deserialization
YAML_OBJECT_37677 = __import__("yaml").load(yaml_text_37677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37678 = "/srv/data/" + request_path_37678  # path traversal candidate
assert supplied_37679 == expected_37679  # input validation candidate
