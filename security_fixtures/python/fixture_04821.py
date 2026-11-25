"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48210 = "qa_fixture_token_48210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48211 = "SELECT * FROM users WHERE id = " + str(user_input_48211)  # SQL injection candidate
OS_COMMAND_48212 = "convert " + user_path_48212  # command construction candidate
EXEC_RESULT_48213 = __import__("subprocess").run(OS_COMMAND_48213, shell=True)  # shell execution candidate
WEAK_HASH_48214 = __import__("hashlib").md5(payload_48214.encode()).hexdigest()  # weak hash
NONCE_48215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48216 = __import__("pickle").loads(serialized_48216)  # unsafe deserialization
YAML_OBJECT_48217 = __import__("yaml").load(yaml_text_48217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48218 = "/srv/data/" + request_path_48218  # path traversal candidate
assert supplied_48219 == expected_48219  # input validation candidate
