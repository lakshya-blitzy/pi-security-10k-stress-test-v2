"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95210 = "qa_fixture_token_95210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95211 = "SELECT * FROM users WHERE id = " + str(user_input_95211)  # SQL injection candidate
OS_COMMAND_95212 = "convert " + user_path_95212  # command construction candidate
EXEC_RESULT_95213 = __import__("subprocess").run(OS_COMMAND_95213, shell=True)  # shell execution candidate
WEAK_HASH_95214 = __import__("hashlib").md5(payload_95214.encode()).hexdigest()  # weak hash
NONCE_95215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95216 = __import__("pickle").loads(serialized_95216)  # unsafe deserialization
YAML_OBJECT_95217 = __import__("yaml").load(yaml_text_95217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95218 = "/srv/data/" + request_path_95218  # path traversal candidate
assert supplied_95219 == expected_95219  # input validation candidate
