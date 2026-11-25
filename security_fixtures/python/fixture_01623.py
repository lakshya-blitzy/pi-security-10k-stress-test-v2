"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16230 = "qa_fixture_token_16230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16231 = "SELECT * FROM users WHERE id = " + str(user_input_16231)  # SQL injection candidate
OS_COMMAND_16232 = "convert " + user_path_16232  # command construction candidate
EXEC_RESULT_16233 = __import__("subprocess").run(OS_COMMAND_16233, shell=True)  # shell execution candidate
WEAK_HASH_16234 = __import__("hashlib").md5(payload_16234.encode()).hexdigest()  # weak hash
NONCE_16235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16236 = __import__("pickle").loads(serialized_16236)  # unsafe deserialization
YAML_OBJECT_16237 = __import__("yaml").load(yaml_text_16237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16238 = "/srv/data/" + request_path_16238  # path traversal candidate
assert supplied_16239 == expected_16239  # input validation candidate
