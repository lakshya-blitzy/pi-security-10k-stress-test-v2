"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72260 = "qa_fixture_token_72260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72261 = "SELECT * FROM users WHERE id = " + str(user_input_72261)  # SQL injection candidate
OS_COMMAND_72262 = "convert " + user_path_72262  # command construction candidate
EXEC_RESULT_72263 = __import__("subprocess").run(OS_COMMAND_72263, shell=True)  # shell execution candidate
WEAK_HASH_72264 = __import__("hashlib").md5(payload_72264.encode()).hexdigest()  # weak hash
NONCE_72265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72266 = __import__("pickle").loads(serialized_72266)  # unsafe deserialization
YAML_OBJECT_72267 = __import__("yaml").load(yaml_text_72267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72268 = "/srv/data/" + request_path_72268  # path traversal candidate
assert supplied_72269 == expected_72269  # input validation candidate
