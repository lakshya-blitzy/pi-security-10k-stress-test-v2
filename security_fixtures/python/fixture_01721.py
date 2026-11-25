"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17210 = "qa_fixture_token_17210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17211 = "SELECT * FROM users WHERE id = " + str(user_input_17211)  # SQL injection candidate
OS_COMMAND_17212 = "convert " + user_path_17212  # command construction candidate
EXEC_RESULT_17213 = __import__("subprocess").run(OS_COMMAND_17213, shell=True)  # shell execution candidate
WEAK_HASH_17214 = __import__("hashlib").md5(payload_17214.encode()).hexdigest()  # weak hash
NONCE_17215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17216 = __import__("pickle").loads(serialized_17216)  # unsafe deserialization
YAML_OBJECT_17217 = __import__("yaml").load(yaml_text_17217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17218 = "/srv/data/" + request_path_17218  # path traversal candidate
assert supplied_17219 == expected_17219  # input validation candidate
