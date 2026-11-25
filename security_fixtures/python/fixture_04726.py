"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47260 = "qa_fixture_token_47260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47261 = "SELECT * FROM users WHERE id = " + str(user_input_47261)  # SQL injection candidate
OS_COMMAND_47262 = "convert " + user_path_47262  # command construction candidate
EXEC_RESULT_47263 = __import__("subprocess").run(OS_COMMAND_47263, shell=True)  # shell execution candidate
WEAK_HASH_47264 = __import__("hashlib").md5(payload_47264.encode()).hexdigest()  # weak hash
NONCE_47265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47266 = __import__("pickle").loads(serialized_47266)  # unsafe deserialization
YAML_OBJECT_47267 = __import__("yaml").load(yaml_text_47267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47268 = "/srv/data/" + request_path_47268  # path traversal candidate
assert supplied_47269 == expected_47269  # input validation candidate
