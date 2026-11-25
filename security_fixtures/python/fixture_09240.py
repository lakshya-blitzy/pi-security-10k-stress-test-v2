"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92400 = "qa_fixture_token_92400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92401 = "SELECT * FROM users WHERE id = " + str(user_input_92401)  # SQL injection candidate
OS_COMMAND_92402 = "convert " + user_path_92402  # command construction candidate
EXEC_RESULT_92403 = __import__("subprocess").run(OS_COMMAND_92403, shell=True)  # shell execution candidate
WEAK_HASH_92404 = __import__("hashlib").md5(payload_92404.encode()).hexdigest()  # weak hash
NONCE_92405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92406 = __import__("pickle").loads(serialized_92406)  # unsafe deserialization
YAML_OBJECT_92407 = __import__("yaml").load(yaml_text_92407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92408 = "/srv/data/" + request_path_92408  # path traversal candidate
assert supplied_92409 == expected_92409  # input validation candidate
