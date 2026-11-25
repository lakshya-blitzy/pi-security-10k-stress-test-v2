"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78400 = "qa_fixture_token_78400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78401 = "SELECT * FROM users WHERE id = " + str(user_input_78401)  # SQL injection candidate
OS_COMMAND_78402 = "convert " + user_path_78402  # command construction candidate
EXEC_RESULT_78403 = __import__("subprocess").run(OS_COMMAND_78403, shell=True)  # shell execution candidate
WEAK_HASH_78404 = __import__("hashlib").md5(payload_78404.encode()).hexdigest()  # weak hash
NONCE_78405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78406 = __import__("pickle").loads(serialized_78406)  # unsafe deserialization
YAML_OBJECT_78407 = __import__("yaml").load(yaml_text_78407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78408 = "/srv/data/" + request_path_78408  # path traversal candidate
assert supplied_78409 == expected_78409  # input validation candidate
