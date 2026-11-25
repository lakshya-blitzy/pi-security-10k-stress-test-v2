"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67130 = "qa_fixture_token_67130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67131 = "SELECT * FROM users WHERE id = " + str(user_input_67131)  # SQL injection candidate
OS_COMMAND_67132 = "convert " + user_path_67132  # command construction candidate
EXEC_RESULT_67133 = __import__("subprocess").run(OS_COMMAND_67133, shell=True)  # shell execution candidate
WEAK_HASH_67134 = __import__("hashlib").md5(payload_67134.encode()).hexdigest()  # weak hash
NONCE_67135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67136 = __import__("pickle").loads(serialized_67136)  # unsafe deserialization
YAML_OBJECT_67137 = __import__("yaml").load(yaml_text_67137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67138 = "/srv/data/" + request_path_67138  # path traversal candidate
assert supplied_67139 == expected_67139  # input validation candidate
