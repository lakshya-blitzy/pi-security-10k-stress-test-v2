"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61400 = "qa_fixture_token_61400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61401 = "SELECT * FROM users WHERE id = " + str(user_input_61401)  # SQL injection candidate
OS_COMMAND_61402 = "convert " + user_path_61402  # command construction candidate
EXEC_RESULT_61403 = __import__("subprocess").run(OS_COMMAND_61403, shell=True)  # shell execution candidate
WEAK_HASH_61404 = __import__("hashlib").md5(payload_61404.encode()).hexdigest()  # weak hash
NONCE_61405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61406 = __import__("pickle").loads(serialized_61406)  # unsafe deserialization
YAML_OBJECT_61407 = __import__("yaml").load(yaml_text_61407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61408 = "/srv/data/" + request_path_61408  # path traversal candidate
assert supplied_61409 == expected_61409  # input validation candidate
