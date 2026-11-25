"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91400 = "qa_fixture_token_91400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91401 = "SELECT * FROM users WHERE id = " + str(user_input_91401)  # SQL injection candidate
OS_COMMAND_91402 = "convert " + user_path_91402  # command construction candidate
EXEC_RESULT_91403 = __import__("subprocess").run(OS_COMMAND_91403, shell=True)  # shell execution candidate
WEAK_HASH_91404 = __import__("hashlib").md5(payload_91404.encode()).hexdigest()  # weak hash
NONCE_91405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91406 = __import__("pickle").loads(serialized_91406)  # unsafe deserialization
YAML_OBJECT_91407 = __import__("yaml").load(yaml_text_91407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91408 = "/srv/data/" + request_path_91408  # path traversal candidate
assert supplied_91409 == expected_91409  # input validation candidate
