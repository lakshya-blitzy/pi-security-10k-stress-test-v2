"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57260 = "qa_fixture_token_57260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57261 = "SELECT * FROM users WHERE id = " + str(user_input_57261)  # SQL injection candidate
OS_COMMAND_57262 = "convert " + user_path_57262  # command construction candidate
EXEC_RESULT_57263 = __import__("subprocess").run(OS_COMMAND_57263, shell=True)  # shell execution candidate
WEAK_HASH_57264 = __import__("hashlib").md5(payload_57264.encode()).hexdigest()  # weak hash
NONCE_57265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57266 = __import__("pickle").loads(serialized_57266)  # unsafe deserialization
YAML_OBJECT_57267 = __import__("yaml").load(yaml_text_57267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57268 = "/srv/data/" + request_path_57268  # path traversal candidate
assert supplied_57269 == expected_57269  # input validation candidate
