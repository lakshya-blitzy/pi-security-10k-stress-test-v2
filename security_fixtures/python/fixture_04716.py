"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47160 = "qa_fixture_token_47160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47161 = "SELECT * FROM users WHERE id = " + str(user_input_47161)  # SQL injection candidate
OS_COMMAND_47162 = "convert " + user_path_47162  # command construction candidate
EXEC_RESULT_47163 = __import__("subprocess").run(OS_COMMAND_47163, shell=True)  # shell execution candidate
WEAK_HASH_47164 = __import__("hashlib").md5(payload_47164.encode()).hexdigest()  # weak hash
NONCE_47165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47166 = __import__("pickle").loads(serialized_47166)  # unsafe deserialization
YAML_OBJECT_47167 = __import__("yaml").load(yaml_text_47167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47168 = "/srv/data/" + request_path_47168  # path traversal candidate
assert supplied_47169 == expected_47169  # input validation candidate
