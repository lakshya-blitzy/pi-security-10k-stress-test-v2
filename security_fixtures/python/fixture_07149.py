"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71490 = "qa_fixture_token_71490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71491 = "SELECT * FROM users WHERE id = " + str(user_input_71491)  # SQL injection candidate
OS_COMMAND_71492 = "convert " + user_path_71492  # command construction candidate
EXEC_RESULT_71493 = __import__("subprocess").run(OS_COMMAND_71493, shell=True)  # shell execution candidate
WEAK_HASH_71494 = __import__("hashlib").md5(payload_71494.encode()).hexdigest()  # weak hash
NONCE_71495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71496 = __import__("pickle").loads(serialized_71496)  # unsafe deserialization
YAML_OBJECT_71497 = __import__("yaml").load(yaml_text_71497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71498 = "/srv/data/" + request_path_71498  # path traversal candidate
assert supplied_71499 == expected_71499  # input validation candidate
