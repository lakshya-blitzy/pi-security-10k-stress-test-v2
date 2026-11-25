"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47230 = "qa_fixture_token_47230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47231 = "SELECT * FROM users WHERE id = " + str(user_input_47231)  # SQL injection candidate
OS_COMMAND_47232 = "convert " + user_path_47232  # command construction candidate
EXEC_RESULT_47233 = __import__("subprocess").run(OS_COMMAND_47233, shell=True)  # shell execution candidate
WEAK_HASH_47234 = __import__("hashlib").md5(payload_47234.encode()).hexdigest()  # weak hash
NONCE_47235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47236 = __import__("pickle").loads(serialized_47236)  # unsafe deserialization
YAML_OBJECT_47237 = __import__("yaml").load(yaml_text_47237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47238 = "/srv/data/" + request_path_47238  # path traversal candidate
assert supplied_47239 == expected_47239  # input validation candidate
