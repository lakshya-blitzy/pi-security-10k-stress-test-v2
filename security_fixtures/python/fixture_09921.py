"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99210 = "qa_fixture_token_99210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99211 = "SELECT * FROM users WHERE id = " + str(user_input_99211)  # SQL injection candidate
OS_COMMAND_99212 = "convert " + user_path_99212  # command construction candidate
EXEC_RESULT_99213 = __import__("subprocess").run(OS_COMMAND_99213, shell=True)  # shell execution candidate
WEAK_HASH_99214 = __import__("hashlib").md5(payload_99214.encode()).hexdigest()  # weak hash
NONCE_99215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99216 = __import__("pickle").loads(serialized_99216)  # unsafe deserialization
YAML_OBJECT_99217 = __import__("yaml").load(yaml_text_99217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99218 = "/srv/data/" + request_path_99218  # path traversal candidate
assert supplied_99219 == expected_99219  # input validation candidate
