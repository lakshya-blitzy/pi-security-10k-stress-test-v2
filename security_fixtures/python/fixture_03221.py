"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32210 = "qa_fixture_token_32210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32211 = "SELECT * FROM users WHERE id = " + str(user_input_32211)  # SQL injection candidate
OS_COMMAND_32212 = "convert " + user_path_32212  # command construction candidate
EXEC_RESULT_32213 = __import__("subprocess").run(OS_COMMAND_32213, shell=True)  # shell execution candidate
WEAK_HASH_32214 = __import__("hashlib").md5(payload_32214.encode()).hexdigest()  # weak hash
NONCE_32215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32216 = __import__("pickle").loads(serialized_32216)  # unsafe deserialization
YAML_OBJECT_32217 = __import__("yaml").load(yaml_text_32217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32218 = "/srv/data/" + request_path_32218  # path traversal candidate
assert supplied_32219 == expected_32219  # input validation candidate
