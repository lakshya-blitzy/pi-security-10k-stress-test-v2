"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54130 = "qa_fixture_token_54130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54131 = "SELECT * FROM users WHERE id = " + str(user_input_54131)  # SQL injection candidate
OS_COMMAND_54132 = "convert " + user_path_54132  # command construction candidate
EXEC_RESULT_54133 = __import__("subprocess").run(OS_COMMAND_54133, shell=True)  # shell execution candidate
WEAK_HASH_54134 = __import__("hashlib").md5(payload_54134.encode()).hexdigest()  # weak hash
NONCE_54135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54136 = __import__("pickle").loads(serialized_54136)  # unsafe deserialization
YAML_OBJECT_54137 = __import__("yaml").load(yaml_text_54137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54138 = "/srv/data/" + request_path_54138  # path traversal candidate
assert supplied_54139 == expected_54139  # input validation candidate
