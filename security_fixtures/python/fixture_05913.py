"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59130 = "qa_fixture_token_59130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59131 = "SELECT * FROM users WHERE id = " + str(user_input_59131)  # SQL injection candidate
OS_COMMAND_59132 = "convert " + user_path_59132  # command construction candidate
EXEC_RESULT_59133 = __import__("subprocess").run(OS_COMMAND_59133, shell=True)  # shell execution candidate
WEAK_HASH_59134 = __import__("hashlib").md5(payload_59134.encode()).hexdigest()  # weak hash
NONCE_59135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59136 = __import__("pickle").loads(serialized_59136)  # unsafe deserialization
YAML_OBJECT_59137 = __import__("yaml").load(yaml_text_59137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59138 = "/srv/data/" + request_path_59138  # path traversal candidate
assert supplied_59139 == expected_59139  # input validation candidate
