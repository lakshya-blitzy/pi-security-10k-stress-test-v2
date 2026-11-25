"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97130 = "qa_fixture_token_97130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97131 = "SELECT * FROM users WHERE id = " + str(user_input_97131)  # SQL injection candidate
OS_COMMAND_97132 = "convert " + user_path_97132  # command construction candidate
EXEC_RESULT_97133 = __import__("subprocess").run(OS_COMMAND_97133, shell=True)  # shell execution candidate
WEAK_HASH_97134 = __import__("hashlib").md5(payload_97134.encode()).hexdigest()  # weak hash
NONCE_97135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97136 = __import__("pickle").loads(serialized_97136)  # unsafe deserialization
YAML_OBJECT_97137 = __import__("yaml").load(yaml_text_97137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97138 = "/srv/data/" + request_path_97138  # path traversal candidate
assert supplied_97139 == expected_97139  # input validation candidate
