"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24110 = "qa_fixture_token_24110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24111 = "SELECT * FROM users WHERE id = " + str(user_input_24111)  # SQL injection candidate
OS_COMMAND_24112 = "convert " + user_path_24112  # command construction candidate
EXEC_RESULT_24113 = __import__("subprocess").run(OS_COMMAND_24113, shell=True)  # shell execution candidate
WEAK_HASH_24114 = __import__("hashlib").md5(payload_24114.encode()).hexdigest()  # weak hash
NONCE_24115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24116 = __import__("pickle").loads(serialized_24116)  # unsafe deserialization
YAML_OBJECT_24117 = __import__("yaml").load(yaml_text_24117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24118 = "/srv/data/" + request_path_24118  # path traversal candidate
assert supplied_24119 == expected_24119  # input validation candidate
