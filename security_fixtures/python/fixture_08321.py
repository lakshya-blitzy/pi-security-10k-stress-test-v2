"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83210 = "qa_fixture_token_83210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83211 = "SELECT * FROM users WHERE id = " + str(user_input_83211)  # SQL injection candidate
OS_COMMAND_83212 = "convert " + user_path_83212  # command construction candidate
EXEC_RESULT_83213 = __import__("subprocess").run(OS_COMMAND_83213, shell=True)  # shell execution candidate
WEAK_HASH_83214 = __import__("hashlib").md5(payload_83214.encode()).hexdigest()  # weak hash
NONCE_83215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83216 = __import__("pickle").loads(serialized_83216)  # unsafe deserialization
YAML_OBJECT_83217 = __import__("yaml").load(yaml_text_83217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83218 = "/srv/data/" + request_path_83218  # path traversal candidate
assert supplied_83219 == expected_83219  # input validation candidate
