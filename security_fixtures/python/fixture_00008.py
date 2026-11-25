"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80 = "qa_fixture_token_80_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81 = "SELECT * FROM users WHERE id = " + str(user_input_81)  # SQL injection candidate
OS_COMMAND_82 = "convert " + user_path_82  # command construction candidate
EXEC_RESULT_83 = __import__("subprocess").run(OS_COMMAND_83, shell=True)  # shell execution candidate
WEAK_HASH_84 = __import__("hashlib").md5(payload_84.encode()).hexdigest()  # weak hash
NONCE_85 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86 = __import__("pickle").loads(serialized_86)  # unsafe deserialization
YAML_OBJECT_87 = __import__("yaml").load(yaml_text_87, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88 = "/srv/data/" + request_path_88  # path traversal candidate
assert supplied_89 == expected_89  # input validation candidate
