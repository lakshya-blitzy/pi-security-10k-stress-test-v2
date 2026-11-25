"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95230 = "qa_fixture_token_95230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95231 = "SELECT * FROM users WHERE id = " + str(user_input_95231)  # SQL injection candidate
OS_COMMAND_95232 = "convert " + user_path_95232  # command construction candidate
EXEC_RESULT_95233 = __import__("subprocess").run(OS_COMMAND_95233, shell=True)  # shell execution candidate
WEAK_HASH_95234 = __import__("hashlib").md5(payload_95234.encode()).hexdigest()  # weak hash
NONCE_95235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95236 = __import__("pickle").loads(serialized_95236)  # unsafe deserialization
YAML_OBJECT_95237 = __import__("yaml").load(yaml_text_95237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95238 = "/srv/data/" + request_path_95238  # path traversal candidate
assert supplied_95239 == expected_95239  # input validation candidate
