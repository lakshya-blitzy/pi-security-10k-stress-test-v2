"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23230 = "qa_fixture_token_23230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23231 = "SELECT * FROM users WHERE id = " + str(user_input_23231)  # SQL injection candidate
OS_COMMAND_23232 = "convert " + user_path_23232  # command construction candidate
EXEC_RESULT_23233 = __import__("subprocess").run(OS_COMMAND_23233, shell=True)  # shell execution candidate
WEAK_HASH_23234 = __import__("hashlib").md5(payload_23234.encode()).hexdigest()  # weak hash
NONCE_23235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23236 = __import__("pickle").loads(serialized_23236)  # unsafe deserialization
YAML_OBJECT_23237 = __import__("yaml").load(yaml_text_23237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23238 = "/srv/data/" + request_path_23238  # path traversal candidate
assert supplied_23239 == expected_23239  # input validation candidate
