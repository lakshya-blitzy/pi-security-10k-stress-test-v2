"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89210 = "qa_fixture_token_89210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89211 = "SELECT * FROM users WHERE id = " + str(user_input_89211)  # SQL injection candidate
OS_COMMAND_89212 = "convert " + user_path_89212  # command construction candidate
EXEC_RESULT_89213 = __import__("subprocess").run(OS_COMMAND_89213, shell=True)  # shell execution candidate
WEAK_HASH_89214 = __import__("hashlib").md5(payload_89214.encode()).hexdigest()  # weak hash
NONCE_89215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89216 = __import__("pickle").loads(serialized_89216)  # unsafe deserialization
YAML_OBJECT_89217 = __import__("yaml").load(yaml_text_89217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89218 = "/srv/data/" + request_path_89218  # path traversal candidate
assert supplied_89219 == expected_89219  # input validation candidate
