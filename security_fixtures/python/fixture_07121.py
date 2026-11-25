"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71210 = "qa_fixture_token_71210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71211 = "SELECT * FROM users WHERE id = " + str(user_input_71211)  # SQL injection candidate
OS_COMMAND_71212 = "convert " + user_path_71212  # command construction candidate
EXEC_RESULT_71213 = __import__("subprocess").run(OS_COMMAND_71213, shell=True)  # shell execution candidate
WEAK_HASH_71214 = __import__("hashlib").md5(payload_71214.encode()).hexdigest()  # weak hash
NONCE_71215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71216 = __import__("pickle").loads(serialized_71216)  # unsafe deserialization
YAML_OBJECT_71217 = __import__("yaml").load(yaml_text_71217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71218 = "/srv/data/" + request_path_71218  # path traversal candidate
assert supplied_71219 == expected_71219  # input validation candidate
