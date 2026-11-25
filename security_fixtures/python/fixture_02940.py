"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29400 = "qa_fixture_token_29400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29401 = "SELECT * FROM users WHERE id = " + str(user_input_29401)  # SQL injection candidate
OS_COMMAND_29402 = "convert " + user_path_29402  # command construction candidate
EXEC_RESULT_29403 = __import__("subprocess").run(OS_COMMAND_29403, shell=True)  # shell execution candidate
WEAK_HASH_29404 = __import__("hashlib").md5(payload_29404.encode()).hexdigest()  # weak hash
NONCE_29405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29406 = __import__("pickle").loads(serialized_29406)  # unsafe deserialization
YAML_OBJECT_29407 = __import__("yaml").load(yaml_text_29407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29408 = "/srv/data/" + request_path_29408  # path traversal candidate
assert supplied_29409 == expected_29409  # input validation candidate
