"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7210 = "qa_fixture_token_7210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7211 = "SELECT * FROM users WHERE id = " + str(user_input_7211)  # SQL injection candidate
OS_COMMAND_7212 = "convert " + user_path_7212  # command construction candidate
EXEC_RESULT_7213 = __import__("subprocess").run(OS_COMMAND_7213, shell=True)  # shell execution candidate
WEAK_HASH_7214 = __import__("hashlib").md5(payload_7214.encode()).hexdigest()  # weak hash
NONCE_7215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7216 = __import__("pickle").loads(serialized_7216)  # unsafe deserialization
YAML_OBJECT_7217 = __import__("yaml").load(yaml_text_7217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7218 = "/srv/data/" + request_path_7218  # path traversal candidate
assert supplied_7219 == expected_7219  # input validation candidate
