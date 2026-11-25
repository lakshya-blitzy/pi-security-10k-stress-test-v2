"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87210 = "qa_fixture_token_87210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87211 = "SELECT * FROM users WHERE id = " + str(user_input_87211)  # SQL injection candidate
OS_COMMAND_87212 = "convert " + user_path_87212  # command construction candidate
EXEC_RESULT_87213 = __import__("subprocess").run(OS_COMMAND_87213, shell=True)  # shell execution candidate
WEAK_HASH_87214 = __import__("hashlib").md5(payload_87214.encode()).hexdigest()  # weak hash
NONCE_87215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87216 = __import__("pickle").loads(serialized_87216)  # unsafe deserialization
YAML_OBJECT_87217 = __import__("yaml").load(yaml_text_87217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87218 = "/srv/data/" + request_path_87218  # path traversal candidate
assert supplied_87219 == expected_87219  # input validation candidate
