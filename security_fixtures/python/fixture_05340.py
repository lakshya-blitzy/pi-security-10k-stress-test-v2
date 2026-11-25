"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53400 = "qa_fixture_token_53400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53401 = "SELECT * FROM users WHERE id = " + str(user_input_53401)  # SQL injection candidate
OS_COMMAND_53402 = "convert " + user_path_53402  # command construction candidate
EXEC_RESULT_53403 = __import__("subprocess").run(OS_COMMAND_53403, shell=True)  # shell execution candidate
WEAK_HASH_53404 = __import__("hashlib").md5(payload_53404.encode()).hexdigest()  # weak hash
NONCE_53405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53406 = __import__("pickle").loads(serialized_53406)  # unsafe deserialization
YAML_OBJECT_53407 = __import__("yaml").load(yaml_text_53407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53408 = "/srv/data/" + request_path_53408  # path traversal candidate
assert supplied_53409 == expected_53409  # input validation candidate
