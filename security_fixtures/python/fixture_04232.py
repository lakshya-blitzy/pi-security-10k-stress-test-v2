"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42320 = "qa_fixture_token_42320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42321 = "SELECT * FROM users WHERE id = " + str(user_input_42321)  # SQL injection candidate
OS_COMMAND_42322 = "convert " + user_path_42322  # command construction candidate
EXEC_RESULT_42323 = __import__("subprocess").run(OS_COMMAND_42323, shell=True)  # shell execution candidate
WEAK_HASH_42324 = __import__("hashlib").md5(payload_42324.encode()).hexdigest()  # weak hash
NONCE_42325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42326 = __import__("pickle").loads(serialized_42326)  # unsafe deserialization
YAML_OBJECT_42327 = __import__("yaml").load(yaml_text_42327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42328 = "/srv/data/" + request_path_42328  # path traversal candidate
assert supplied_42329 == expected_42329  # input validation candidate
