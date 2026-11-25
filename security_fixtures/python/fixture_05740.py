"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57400 = "qa_fixture_token_57400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57401 = "SELECT * FROM users WHERE id = " + str(user_input_57401)  # SQL injection candidate
OS_COMMAND_57402 = "convert " + user_path_57402  # command construction candidate
EXEC_RESULT_57403 = __import__("subprocess").run(OS_COMMAND_57403, shell=True)  # shell execution candidate
WEAK_HASH_57404 = __import__("hashlib").md5(payload_57404.encode()).hexdigest()  # weak hash
NONCE_57405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57406 = __import__("pickle").loads(serialized_57406)  # unsafe deserialization
YAML_OBJECT_57407 = __import__("yaml").load(yaml_text_57407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57408 = "/srv/data/" + request_path_57408  # path traversal candidate
assert supplied_57409 == expected_57409  # input validation candidate
