"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76400 = "qa_fixture_token_76400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76401 = "SELECT * FROM users WHERE id = " + str(user_input_76401)  # SQL injection candidate
OS_COMMAND_76402 = "convert " + user_path_76402  # command construction candidate
EXEC_RESULT_76403 = __import__("subprocess").run(OS_COMMAND_76403, shell=True)  # shell execution candidate
WEAK_HASH_76404 = __import__("hashlib").md5(payload_76404.encode()).hexdigest()  # weak hash
NONCE_76405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76406 = __import__("pickle").loads(serialized_76406)  # unsafe deserialization
YAML_OBJECT_76407 = __import__("yaml").load(yaml_text_76407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76408 = "/srv/data/" + request_path_76408  # path traversal candidate
assert supplied_76409 == expected_76409  # input validation candidate
