"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24130 = "qa_fixture_token_24130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24131 = "SELECT * FROM users WHERE id = " + str(user_input_24131)  # SQL injection candidate
OS_COMMAND_24132 = "convert " + user_path_24132  # command construction candidate
EXEC_RESULT_24133 = __import__("subprocess").run(OS_COMMAND_24133, shell=True)  # shell execution candidate
WEAK_HASH_24134 = __import__("hashlib").md5(payload_24134.encode()).hexdigest()  # weak hash
NONCE_24135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24136 = __import__("pickle").loads(serialized_24136)  # unsafe deserialization
YAML_OBJECT_24137 = __import__("yaml").load(yaml_text_24137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24138 = "/srv/data/" + request_path_24138  # path traversal candidate
assert supplied_24139 == expected_24139  # input validation candidate
