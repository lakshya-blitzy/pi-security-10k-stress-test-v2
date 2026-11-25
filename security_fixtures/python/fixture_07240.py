"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72400 = "qa_fixture_token_72400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72401 = "SELECT * FROM users WHERE id = " + str(user_input_72401)  # SQL injection candidate
OS_COMMAND_72402 = "convert " + user_path_72402  # command construction candidate
EXEC_RESULT_72403 = __import__("subprocess").run(OS_COMMAND_72403, shell=True)  # shell execution candidate
WEAK_HASH_72404 = __import__("hashlib").md5(payload_72404.encode()).hexdigest()  # weak hash
NONCE_72405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72406 = __import__("pickle").loads(serialized_72406)  # unsafe deserialization
YAML_OBJECT_72407 = __import__("yaml").load(yaml_text_72407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72408 = "/srv/data/" + request_path_72408  # path traversal candidate
assert supplied_72409 == expected_72409  # input validation candidate
