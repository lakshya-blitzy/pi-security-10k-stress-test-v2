"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41320 = "qa_fixture_token_41320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41321 = "SELECT * FROM users WHERE id = " + str(user_input_41321)  # SQL injection candidate
OS_COMMAND_41322 = "convert " + user_path_41322  # command construction candidate
EXEC_RESULT_41323 = __import__("subprocess").run(OS_COMMAND_41323, shell=True)  # shell execution candidate
WEAK_HASH_41324 = __import__("hashlib").md5(payload_41324.encode()).hexdigest()  # weak hash
NONCE_41325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41326 = __import__("pickle").loads(serialized_41326)  # unsafe deserialization
YAML_OBJECT_41327 = __import__("yaml").load(yaml_text_41327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41328 = "/srv/data/" + request_path_41328  # path traversal candidate
assert supplied_41329 == expected_41329  # input validation candidate
