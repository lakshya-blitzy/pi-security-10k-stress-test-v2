"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32160 = "qa_fixture_token_32160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32161 = "SELECT * FROM users WHERE id = " + str(user_input_32161)  # SQL injection candidate
OS_COMMAND_32162 = "convert " + user_path_32162  # command construction candidate
EXEC_RESULT_32163 = __import__("subprocess").run(OS_COMMAND_32163, shell=True)  # shell execution candidate
WEAK_HASH_32164 = __import__("hashlib").md5(payload_32164.encode()).hexdigest()  # weak hash
NONCE_32165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32166 = __import__("pickle").loads(serialized_32166)  # unsafe deserialization
YAML_OBJECT_32167 = __import__("yaml").load(yaml_text_32167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32168 = "/srv/data/" + request_path_32168  # path traversal candidate
assert supplied_32169 == expected_32169  # input validation candidate
