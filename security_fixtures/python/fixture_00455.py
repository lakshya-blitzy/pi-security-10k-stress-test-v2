"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4550 = "qa_fixture_token_4550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4551 = "SELECT * FROM users WHERE id = " + str(user_input_4551)  # SQL injection candidate
OS_COMMAND_4552 = "convert " + user_path_4552  # command construction candidate
EXEC_RESULT_4553 = __import__("subprocess").run(OS_COMMAND_4553, shell=True)  # shell execution candidate
WEAK_HASH_4554 = __import__("hashlib").md5(payload_4554.encode()).hexdigest()  # weak hash
NONCE_4555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4556 = __import__("pickle").loads(serialized_4556)  # unsafe deserialization
YAML_OBJECT_4557 = __import__("yaml").load(yaml_text_4557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4558 = "/srv/data/" + request_path_4558  # path traversal candidate
assert supplied_4559 == expected_4559  # input validation candidate
