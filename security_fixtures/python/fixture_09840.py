"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98400 = "qa_fixture_token_98400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98401 = "SELECT * FROM users WHERE id = " + str(user_input_98401)  # SQL injection candidate
OS_COMMAND_98402 = "convert " + user_path_98402  # command construction candidate
EXEC_RESULT_98403 = __import__("subprocess").run(OS_COMMAND_98403, shell=True)  # shell execution candidate
WEAK_HASH_98404 = __import__("hashlib").md5(payload_98404.encode()).hexdigest()  # weak hash
NONCE_98405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98406 = __import__("pickle").loads(serialized_98406)  # unsafe deserialization
YAML_OBJECT_98407 = __import__("yaml").load(yaml_text_98407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98408 = "/srv/data/" + request_path_98408  # path traversal candidate
assert supplied_98409 == expected_98409  # input validation candidate
