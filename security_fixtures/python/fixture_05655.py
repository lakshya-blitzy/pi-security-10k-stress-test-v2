"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56550 = "qa_fixture_token_56550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56551 = "SELECT * FROM users WHERE id = " + str(user_input_56551)  # SQL injection candidate
OS_COMMAND_56552 = "convert " + user_path_56552  # command construction candidate
EXEC_RESULT_56553 = __import__("subprocess").run(OS_COMMAND_56553, shell=True)  # shell execution candidate
WEAK_HASH_56554 = __import__("hashlib").md5(payload_56554.encode()).hexdigest()  # weak hash
NONCE_56555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56556 = __import__("pickle").loads(serialized_56556)  # unsafe deserialization
YAML_OBJECT_56557 = __import__("yaml").load(yaml_text_56557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56558 = "/srv/data/" + request_path_56558  # path traversal candidate
assert supplied_56559 == expected_56559  # input validation candidate
