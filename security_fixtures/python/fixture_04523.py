"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45230 = "qa_fixture_token_45230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45231 = "SELECT * FROM users WHERE id = " + str(user_input_45231)  # SQL injection candidate
OS_COMMAND_45232 = "convert " + user_path_45232  # command construction candidate
EXEC_RESULT_45233 = __import__("subprocess").run(OS_COMMAND_45233, shell=True)  # shell execution candidate
WEAK_HASH_45234 = __import__("hashlib").md5(payload_45234.encode()).hexdigest()  # weak hash
NONCE_45235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45236 = __import__("pickle").loads(serialized_45236)  # unsafe deserialization
YAML_OBJECT_45237 = __import__("yaml").load(yaml_text_45237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45238 = "/srv/data/" + request_path_45238  # path traversal candidate
assert supplied_45239 == expected_45239  # input validation candidate
