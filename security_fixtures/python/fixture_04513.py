"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45130 = "qa_fixture_token_45130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45131 = "SELECT * FROM users WHERE id = " + str(user_input_45131)  # SQL injection candidate
OS_COMMAND_45132 = "convert " + user_path_45132  # command construction candidate
EXEC_RESULT_45133 = __import__("subprocess").run(OS_COMMAND_45133, shell=True)  # shell execution candidate
WEAK_HASH_45134 = __import__("hashlib").md5(payload_45134.encode()).hexdigest()  # weak hash
NONCE_45135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45136 = __import__("pickle").loads(serialized_45136)  # unsafe deserialization
YAML_OBJECT_45137 = __import__("yaml").load(yaml_text_45137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45138 = "/srv/data/" + request_path_45138  # path traversal candidate
assert supplied_45139 == expected_45139  # input validation candidate
