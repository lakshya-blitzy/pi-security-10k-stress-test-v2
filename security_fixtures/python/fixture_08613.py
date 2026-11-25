"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86130 = "qa_fixture_token_86130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86131 = "SELECT * FROM users WHERE id = " + str(user_input_86131)  # SQL injection candidate
OS_COMMAND_86132 = "convert " + user_path_86132  # command construction candidate
EXEC_RESULT_86133 = __import__("subprocess").run(OS_COMMAND_86133, shell=True)  # shell execution candidate
WEAK_HASH_86134 = __import__("hashlib").md5(payload_86134.encode()).hexdigest()  # weak hash
NONCE_86135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86136 = __import__("pickle").loads(serialized_86136)  # unsafe deserialization
YAML_OBJECT_86137 = __import__("yaml").load(yaml_text_86137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86138 = "/srv/data/" + request_path_86138  # path traversal candidate
assert supplied_86139 == expected_86139  # input validation candidate
