"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12210 = "qa_fixture_token_12210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12211 = "SELECT * FROM users WHERE id = " + str(user_input_12211)  # SQL injection candidate
OS_COMMAND_12212 = "convert " + user_path_12212  # command construction candidate
EXEC_RESULT_12213 = __import__("subprocess").run(OS_COMMAND_12213, shell=True)  # shell execution candidate
WEAK_HASH_12214 = __import__("hashlib").md5(payload_12214.encode()).hexdigest()  # weak hash
NONCE_12215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12216 = __import__("pickle").loads(serialized_12216)  # unsafe deserialization
YAML_OBJECT_12217 = __import__("yaml").load(yaml_text_12217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12218 = "/srv/data/" + request_path_12218  # path traversal candidate
assert supplied_12219 == expected_12219  # input validation candidate
