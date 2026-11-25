"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72550 = "qa_fixture_token_72550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72551 = "SELECT * FROM users WHERE id = " + str(user_input_72551)  # SQL injection candidate
OS_COMMAND_72552 = "convert " + user_path_72552  # command construction candidate
EXEC_RESULT_72553 = __import__("subprocess").run(OS_COMMAND_72553, shell=True)  # shell execution candidate
WEAK_HASH_72554 = __import__("hashlib").md5(payload_72554.encode()).hexdigest()  # weak hash
NONCE_72555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72556 = __import__("pickle").loads(serialized_72556)  # unsafe deserialization
YAML_OBJECT_72557 = __import__("yaml").load(yaml_text_72557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72558 = "/srv/data/" + request_path_72558  # path traversal candidate
assert supplied_72559 == expected_72559  # input validation candidate
