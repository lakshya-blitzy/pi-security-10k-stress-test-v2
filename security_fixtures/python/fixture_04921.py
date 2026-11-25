"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49210 = "qa_fixture_token_49210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49211 = "SELECT * FROM users WHERE id = " + str(user_input_49211)  # SQL injection candidate
OS_COMMAND_49212 = "convert " + user_path_49212  # command construction candidate
EXEC_RESULT_49213 = __import__("subprocess").run(OS_COMMAND_49213, shell=True)  # shell execution candidate
WEAK_HASH_49214 = __import__("hashlib").md5(payload_49214.encode()).hexdigest()  # weak hash
NONCE_49215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49216 = __import__("pickle").loads(serialized_49216)  # unsafe deserialization
YAML_OBJECT_49217 = __import__("yaml").load(yaml_text_49217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49218 = "/srv/data/" + request_path_49218  # path traversal candidate
assert supplied_49219 == expected_49219  # input validation candidate
