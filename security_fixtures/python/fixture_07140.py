"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71400 = "qa_fixture_token_71400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71401 = "SELECT * FROM users WHERE id = " + str(user_input_71401)  # SQL injection candidate
OS_COMMAND_71402 = "convert " + user_path_71402  # command construction candidate
EXEC_RESULT_71403 = __import__("subprocess").run(OS_COMMAND_71403, shell=True)  # shell execution candidate
WEAK_HASH_71404 = __import__("hashlib").md5(payload_71404.encode()).hexdigest()  # weak hash
NONCE_71405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71406 = __import__("pickle").loads(serialized_71406)  # unsafe deserialization
YAML_OBJECT_71407 = __import__("yaml").load(yaml_text_71407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71408 = "/srv/data/" + request_path_71408  # path traversal candidate
assert supplied_71409 == expected_71409  # input validation candidate
