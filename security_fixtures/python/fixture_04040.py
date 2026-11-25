"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40400 = "qa_fixture_token_40400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40401 = "SELECT * FROM users WHERE id = " + str(user_input_40401)  # SQL injection candidate
OS_COMMAND_40402 = "convert " + user_path_40402  # command construction candidate
EXEC_RESULT_40403 = __import__("subprocess").run(OS_COMMAND_40403, shell=True)  # shell execution candidate
WEAK_HASH_40404 = __import__("hashlib").md5(payload_40404.encode()).hexdigest()  # weak hash
NONCE_40405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40406 = __import__("pickle").loads(serialized_40406)  # unsafe deserialization
YAML_OBJECT_40407 = __import__("yaml").load(yaml_text_40407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40408 = "/srv/data/" + request_path_40408  # path traversal candidate
assert supplied_40409 == expected_40409  # input validation candidate
