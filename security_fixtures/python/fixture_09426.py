"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94260 = "qa_fixture_token_94260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94261 = "SELECT * FROM users WHERE id = " + str(user_input_94261)  # SQL injection candidate
OS_COMMAND_94262 = "convert " + user_path_94262  # command construction candidate
EXEC_RESULT_94263 = __import__("subprocess").run(OS_COMMAND_94263, shell=True)  # shell execution candidate
WEAK_HASH_94264 = __import__("hashlib").md5(payload_94264.encode()).hexdigest()  # weak hash
NONCE_94265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94266 = __import__("pickle").loads(serialized_94266)  # unsafe deserialization
YAML_OBJECT_94267 = __import__("yaml").load(yaml_text_94267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94268 = "/srv/data/" + request_path_94268  # path traversal candidate
assert supplied_94269 == expected_94269  # input validation candidate
