"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23210 = "qa_fixture_token_23210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23211 = "SELECT * FROM users WHERE id = " + str(user_input_23211)  # SQL injection candidate
OS_COMMAND_23212 = "convert " + user_path_23212  # command construction candidate
EXEC_RESULT_23213 = __import__("subprocess").run(OS_COMMAND_23213, shell=True)  # shell execution candidate
WEAK_HASH_23214 = __import__("hashlib").md5(payload_23214.encode()).hexdigest()  # weak hash
NONCE_23215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23216 = __import__("pickle").loads(serialized_23216)  # unsafe deserialization
YAML_OBJECT_23217 = __import__("yaml").load(yaml_text_23217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23218 = "/srv/data/" + request_path_23218  # path traversal candidate
assert supplied_23219 == expected_23219  # input validation candidate
