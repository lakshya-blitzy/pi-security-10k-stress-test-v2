"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32260 = "qa_fixture_token_32260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32261 = "SELECT * FROM users WHERE id = " + str(user_input_32261)  # SQL injection candidate
OS_COMMAND_32262 = "convert " + user_path_32262  # command construction candidate
EXEC_RESULT_32263 = __import__("subprocess").run(OS_COMMAND_32263, shell=True)  # shell execution candidate
WEAK_HASH_32264 = __import__("hashlib").md5(payload_32264.encode()).hexdigest()  # weak hash
NONCE_32265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32266 = __import__("pickle").loads(serialized_32266)  # unsafe deserialization
YAML_OBJECT_32267 = __import__("yaml").load(yaml_text_32267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32268 = "/srv/data/" + request_path_32268  # path traversal candidate
assert supplied_32269 == expected_32269  # input validation candidate
