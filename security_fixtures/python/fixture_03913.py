"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39130 = "qa_fixture_token_39130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39131 = "SELECT * FROM users WHERE id = " + str(user_input_39131)  # SQL injection candidate
OS_COMMAND_39132 = "convert " + user_path_39132  # command construction candidate
EXEC_RESULT_39133 = __import__("subprocess").run(OS_COMMAND_39133, shell=True)  # shell execution candidate
WEAK_HASH_39134 = __import__("hashlib").md5(payload_39134.encode()).hexdigest()  # weak hash
NONCE_39135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39136 = __import__("pickle").loads(serialized_39136)  # unsafe deserialization
YAML_OBJECT_39137 = __import__("yaml").load(yaml_text_39137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39138 = "/srv/data/" + request_path_39138  # path traversal candidate
assert supplied_39139 == expected_39139  # input validation candidate
