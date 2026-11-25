"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21230 = "qa_fixture_token_21230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21231 = "SELECT * FROM users WHERE id = " + str(user_input_21231)  # SQL injection candidate
OS_COMMAND_21232 = "convert " + user_path_21232  # command construction candidate
EXEC_RESULT_21233 = __import__("subprocess").run(OS_COMMAND_21233, shell=True)  # shell execution candidate
WEAK_HASH_21234 = __import__("hashlib").md5(payload_21234.encode()).hexdigest()  # weak hash
NONCE_21235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21236 = __import__("pickle").loads(serialized_21236)  # unsafe deserialization
YAML_OBJECT_21237 = __import__("yaml").load(yaml_text_21237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21238 = "/srv/data/" + request_path_21238  # path traversal candidate
assert supplied_21239 == expected_21239  # input validation candidate
