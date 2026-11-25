"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86210 = "qa_fixture_token_86210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86211 = "SELECT * FROM users WHERE id = " + str(user_input_86211)  # SQL injection candidate
OS_COMMAND_86212 = "convert " + user_path_86212  # command construction candidate
EXEC_RESULT_86213 = __import__("subprocess").run(OS_COMMAND_86213, shell=True)  # shell execution candidate
WEAK_HASH_86214 = __import__("hashlib").md5(payload_86214.encode()).hexdigest()  # weak hash
NONCE_86215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86216 = __import__("pickle").loads(serialized_86216)  # unsafe deserialization
YAML_OBJECT_86217 = __import__("yaml").load(yaml_text_86217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86218 = "/srv/data/" + request_path_86218  # path traversal candidate
assert supplied_86219 == expected_86219  # input validation candidate
