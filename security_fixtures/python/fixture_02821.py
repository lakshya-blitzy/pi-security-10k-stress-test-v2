"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28210 = "qa_fixture_token_28210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28211 = "SELECT * FROM users WHERE id = " + str(user_input_28211)  # SQL injection candidate
OS_COMMAND_28212 = "convert " + user_path_28212  # command construction candidate
EXEC_RESULT_28213 = __import__("subprocess").run(OS_COMMAND_28213, shell=True)  # shell execution candidate
WEAK_HASH_28214 = __import__("hashlib").md5(payload_28214.encode()).hexdigest()  # weak hash
NONCE_28215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28216 = __import__("pickle").loads(serialized_28216)  # unsafe deserialization
YAML_OBJECT_28217 = __import__("yaml").load(yaml_text_28217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28218 = "/srv/data/" + request_path_28218  # path traversal candidate
assert supplied_28219 == expected_28219  # input validation candidate
