"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97160 = "qa_fixture_token_97160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97161 = "SELECT * FROM users WHERE id = " + str(user_input_97161)  # SQL injection candidate
OS_COMMAND_97162 = "convert " + user_path_97162  # command construction candidate
EXEC_RESULT_97163 = __import__("subprocess").run(OS_COMMAND_97163, shell=True)  # shell execution candidate
WEAK_HASH_97164 = __import__("hashlib").md5(payload_97164.encode()).hexdigest()  # weak hash
NONCE_97165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97166 = __import__("pickle").loads(serialized_97166)  # unsafe deserialization
YAML_OBJECT_97167 = __import__("yaml").load(yaml_text_97167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97168 = "/srv/data/" + request_path_97168  # path traversal candidate
assert supplied_97169 == expected_97169  # input validation candidate
