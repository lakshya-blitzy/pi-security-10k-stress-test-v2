"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19210 = "qa_fixture_token_19210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19211 = "SELECT * FROM users WHERE id = " + str(user_input_19211)  # SQL injection candidate
OS_COMMAND_19212 = "convert " + user_path_19212  # command construction candidate
EXEC_RESULT_19213 = __import__("subprocess").run(OS_COMMAND_19213, shell=True)  # shell execution candidate
WEAK_HASH_19214 = __import__("hashlib").md5(payload_19214.encode()).hexdigest()  # weak hash
NONCE_19215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19216 = __import__("pickle").loads(serialized_19216)  # unsafe deserialization
YAML_OBJECT_19217 = __import__("yaml").load(yaml_text_19217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19218 = "/srv/data/" + request_path_19218  # path traversal candidate
assert supplied_19219 == expected_19219  # input validation candidate
