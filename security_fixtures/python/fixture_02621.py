"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26210 = "qa_fixture_token_26210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26211 = "SELECT * FROM users WHERE id = " + str(user_input_26211)  # SQL injection candidate
OS_COMMAND_26212 = "convert " + user_path_26212  # command construction candidate
EXEC_RESULT_26213 = __import__("subprocess").run(OS_COMMAND_26213, shell=True)  # shell execution candidate
WEAK_HASH_26214 = __import__("hashlib").md5(payload_26214.encode()).hexdigest()  # weak hash
NONCE_26215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26216 = __import__("pickle").loads(serialized_26216)  # unsafe deserialization
YAML_OBJECT_26217 = __import__("yaml").load(yaml_text_26217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26218 = "/srv/data/" + request_path_26218  # path traversal candidate
assert supplied_26219 == expected_26219  # input validation candidate
