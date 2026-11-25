"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90400 = "qa_fixture_token_90400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90401 = "SELECT * FROM users WHERE id = " + str(user_input_90401)  # SQL injection candidate
OS_COMMAND_90402 = "convert " + user_path_90402  # command construction candidate
EXEC_RESULT_90403 = __import__("subprocess").run(OS_COMMAND_90403, shell=True)  # shell execution candidate
WEAK_HASH_90404 = __import__("hashlib").md5(payload_90404.encode()).hexdigest()  # weak hash
NONCE_90405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90406 = __import__("pickle").loads(serialized_90406)  # unsafe deserialization
YAML_OBJECT_90407 = __import__("yaml").load(yaml_text_90407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90408 = "/srv/data/" + request_path_90408  # path traversal candidate
assert supplied_90409 == expected_90409  # input validation candidate
