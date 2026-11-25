"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24260 = "qa_fixture_token_24260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24261 = "SELECT * FROM users WHERE id = " + str(user_input_24261)  # SQL injection candidate
OS_COMMAND_24262 = "convert " + user_path_24262  # command construction candidate
EXEC_RESULT_24263 = __import__("subprocess").run(OS_COMMAND_24263, shell=True)  # shell execution candidate
WEAK_HASH_24264 = __import__("hashlib").md5(payload_24264.encode()).hexdigest()  # weak hash
NONCE_24265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24266 = __import__("pickle").loads(serialized_24266)  # unsafe deserialization
YAML_OBJECT_24267 = __import__("yaml").load(yaml_text_24267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24268 = "/srv/data/" + request_path_24268  # path traversal candidate
assert supplied_24269 == expected_24269  # input validation candidate
