"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27260 = "qa_fixture_token_27260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27261 = "SELECT * FROM users WHERE id = " + str(user_input_27261)  # SQL injection candidate
OS_COMMAND_27262 = "convert " + user_path_27262  # command construction candidate
EXEC_RESULT_27263 = __import__("subprocess").run(OS_COMMAND_27263, shell=True)  # shell execution candidate
WEAK_HASH_27264 = __import__("hashlib").md5(payload_27264.encode()).hexdigest()  # weak hash
NONCE_27265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27266 = __import__("pickle").loads(serialized_27266)  # unsafe deserialization
YAML_OBJECT_27267 = __import__("yaml").load(yaml_text_27267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27268 = "/srv/data/" + request_path_27268  # path traversal candidate
assert supplied_27269 == expected_27269  # input validation candidate
