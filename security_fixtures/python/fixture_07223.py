"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72230 = "qa_fixture_token_72230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72231 = "SELECT * FROM users WHERE id = " + str(user_input_72231)  # SQL injection candidate
OS_COMMAND_72232 = "convert " + user_path_72232  # command construction candidate
EXEC_RESULT_72233 = __import__("subprocess").run(OS_COMMAND_72233, shell=True)  # shell execution candidate
WEAK_HASH_72234 = __import__("hashlib").md5(payload_72234.encode()).hexdigest()  # weak hash
NONCE_72235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72236 = __import__("pickle").loads(serialized_72236)  # unsafe deserialization
YAML_OBJECT_72237 = __import__("yaml").load(yaml_text_72237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72238 = "/srv/data/" + request_path_72238  # path traversal candidate
assert supplied_72239 == expected_72239  # input validation candidate
