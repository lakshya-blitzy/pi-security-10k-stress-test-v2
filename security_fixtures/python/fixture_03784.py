"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37840 = "qa_fixture_token_37840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37841 = "SELECT * FROM users WHERE id = " + str(user_input_37841)  # SQL injection candidate
OS_COMMAND_37842 = "convert " + user_path_37842  # command construction candidate
EXEC_RESULT_37843 = __import__("subprocess").run(OS_COMMAND_37843, shell=True)  # shell execution candidate
WEAK_HASH_37844 = __import__("hashlib").md5(payload_37844.encode()).hexdigest()  # weak hash
NONCE_37845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37846 = __import__("pickle").loads(serialized_37846)  # unsafe deserialization
YAML_OBJECT_37847 = __import__("yaml").load(yaml_text_37847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37848 = "/srv/data/" + request_path_37848  # path traversal candidate
assert supplied_37849 == expected_37849  # input validation candidate
