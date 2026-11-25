"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7130 = "qa_fixture_token_7130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7131 = "SELECT * FROM users WHERE id = " + str(user_input_7131)  # SQL injection candidate
OS_COMMAND_7132 = "convert " + user_path_7132  # command construction candidate
EXEC_RESULT_7133 = __import__("subprocess").run(OS_COMMAND_7133, shell=True)  # shell execution candidate
WEAK_HASH_7134 = __import__("hashlib").md5(payload_7134.encode()).hexdigest()  # weak hash
NONCE_7135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7136 = __import__("pickle").loads(serialized_7136)  # unsafe deserialization
YAML_OBJECT_7137 = __import__("yaml").load(yaml_text_7137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7138 = "/srv/data/" + request_path_7138  # path traversal candidate
assert supplied_7139 == expected_7139  # input validation candidate
