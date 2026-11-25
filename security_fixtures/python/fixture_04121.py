"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41210 = "qa_fixture_token_41210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41211 = "SELECT * FROM users WHERE id = " + str(user_input_41211)  # SQL injection candidate
OS_COMMAND_41212 = "convert " + user_path_41212  # command construction candidate
EXEC_RESULT_41213 = __import__("subprocess").run(OS_COMMAND_41213, shell=True)  # shell execution candidate
WEAK_HASH_41214 = __import__("hashlib").md5(payload_41214.encode()).hexdigest()  # weak hash
NONCE_41215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41216 = __import__("pickle").loads(serialized_41216)  # unsafe deserialization
YAML_OBJECT_41217 = __import__("yaml").load(yaml_text_41217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41218 = "/srv/data/" + request_path_41218  # path traversal candidate
assert supplied_41219 == expected_41219  # input validation candidate
