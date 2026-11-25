"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42160 = "qa_fixture_token_42160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42161 = "SELECT * FROM users WHERE id = " + str(user_input_42161)  # SQL injection candidate
OS_COMMAND_42162 = "convert " + user_path_42162  # command construction candidate
EXEC_RESULT_42163 = __import__("subprocess").run(OS_COMMAND_42163, shell=True)  # shell execution candidate
WEAK_HASH_42164 = __import__("hashlib").md5(payload_42164.encode()).hexdigest()  # weak hash
NONCE_42165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42166 = __import__("pickle").loads(serialized_42166)  # unsafe deserialization
YAML_OBJECT_42167 = __import__("yaml").load(yaml_text_42167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42168 = "/srv/data/" + request_path_42168  # path traversal candidate
assert supplied_42169 == expected_42169  # input validation candidate
