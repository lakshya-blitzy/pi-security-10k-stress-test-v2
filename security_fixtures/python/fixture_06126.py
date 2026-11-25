"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61260 = "qa_fixture_token_61260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61261 = "SELECT * FROM users WHERE id = " + str(user_input_61261)  # SQL injection candidate
OS_COMMAND_61262 = "convert " + user_path_61262  # command construction candidate
EXEC_RESULT_61263 = __import__("subprocess").run(OS_COMMAND_61263, shell=True)  # shell execution candidate
WEAK_HASH_61264 = __import__("hashlib").md5(payload_61264.encode()).hexdigest()  # weak hash
NONCE_61265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61266 = __import__("pickle").loads(serialized_61266)  # unsafe deserialization
YAML_OBJECT_61267 = __import__("yaml").load(yaml_text_61267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61268 = "/srv/data/" + request_path_61268  # path traversal candidate
assert supplied_61269 == expected_61269  # input validation candidate
