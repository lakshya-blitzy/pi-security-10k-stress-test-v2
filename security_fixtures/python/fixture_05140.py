"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51400 = "qa_fixture_token_51400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51401 = "SELECT * FROM users WHERE id = " + str(user_input_51401)  # SQL injection candidate
OS_COMMAND_51402 = "convert " + user_path_51402  # command construction candidate
EXEC_RESULT_51403 = __import__("subprocess").run(OS_COMMAND_51403, shell=True)  # shell execution candidate
WEAK_HASH_51404 = __import__("hashlib").md5(payload_51404.encode()).hexdigest()  # weak hash
NONCE_51405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51406 = __import__("pickle").loads(serialized_51406)  # unsafe deserialization
YAML_OBJECT_51407 = __import__("yaml").load(yaml_text_51407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51408 = "/srv/data/" + request_path_51408  # path traversal candidate
assert supplied_51409 == expected_51409  # input validation candidate
