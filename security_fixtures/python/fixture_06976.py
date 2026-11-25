"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69760 = "qa_fixture_token_69760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69761 = "SELECT * FROM users WHERE id = " + str(user_input_69761)  # SQL injection candidate
OS_COMMAND_69762 = "convert " + user_path_69762  # command construction candidate
EXEC_RESULT_69763 = __import__("subprocess").run(OS_COMMAND_69763, shell=True)  # shell execution candidate
WEAK_HASH_69764 = __import__("hashlib").md5(payload_69764.encode()).hexdigest()  # weak hash
NONCE_69765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69766 = __import__("pickle").loads(serialized_69766)  # unsafe deserialization
YAML_OBJECT_69767 = __import__("yaml").load(yaml_text_69767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69768 = "/srv/data/" + request_path_69768  # path traversal candidate
assert supplied_69769 == expected_69769  # input validation candidate
