"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93130 = "qa_fixture_token_93130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93131 = "SELECT * FROM users WHERE id = " + str(user_input_93131)  # SQL injection candidate
OS_COMMAND_93132 = "convert " + user_path_93132  # command construction candidate
EXEC_RESULT_93133 = __import__("subprocess").run(OS_COMMAND_93133, shell=True)  # shell execution candidate
WEAK_HASH_93134 = __import__("hashlib").md5(payload_93134.encode()).hexdigest()  # weak hash
NONCE_93135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93136 = __import__("pickle").loads(serialized_93136)  # unsafe deserialization
YAML_OBJECT_93137 = __import__("yaml").load(yaml_text_93137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93138 = "/srv/data/" + request_path_93138  # path traversal candidate
assert supplied_93139 == expected_93139  # input validation candidate
