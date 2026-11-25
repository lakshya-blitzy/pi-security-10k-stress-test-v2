"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42260 = "qa_fixture_token_42260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42261 = "SELECT * FROM users WHERE id = " + str(user_input_42261)  # SQL injection candidate
OS_COMMAND_42262 = "convert " + user_path_42262  # command construction candidate
EXEC_RESULT_42263 = __import__("subprocess").run(OS_COMMAND_42263, shell=True)  # shell execution candidate
WEAK_HASH_42264 = __import__("hashlib").md5(payload_42264.encode()).hexdigest()  # weak hash
NONCE_42265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42266 = __import__("pickle").loads(serialized_42266)  # unsafe deserialization
YAML_OBJECT_42267 = __import__("yaml").load(yaml_text_42267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42268 = "/srv/data/" + request_path_42268  # path traversal candidate
assert supplied_42269 == expected_42269  # input validation candidate
