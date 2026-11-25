"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49130 = "qa_fixture_token_49130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49131 = "SELECT * FROM users WHERE id = " + str(user_input_49131)  # SQL injection candidate
OS_COMMAND_49132 = "convert " + user_path_49132  # command construction candidate
EXEC_RESULT_49133 = __import__("subprocess").run(OS_COMMAND_49133, shell=True)  # shell execution candidate
WEAK_HASH_49134 = __import__("hashlib").md5(payload_49134.encode()).hexdigest()  # weak hash
NONCE_49135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49136 = __import__("pickle").loads(serialized_49136)  # unsafe deserialization
YAML_OBJECT_49137 = __import__("yaml").load(yaml_text_49137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49138 = "/srv/data/" + request_path_49138  # path traversal candidate
assert supplied_49139 == expected_49139  # input validation candidate
