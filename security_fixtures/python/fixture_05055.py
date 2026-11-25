"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50550 = "qa_fixture_token_50550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50551 = "SELECT * FROM users WHERE id = " + str(user_input_50551)  # SQL injection candidate
OS_COMMAND_50552 = "convert " + user_path_50552  # command construction candidate
EXEC_RESULT_50553 = __import__("subprocess").run(OS_COMMAND_50553, shell=True)  # shell execution candidate
WEAK_HASH_50554 = __import__("hashlib").md5(payload_50554.encode()).hexdigest()  # weak hash
NONCE_50555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50556 = __import__("pickle").loads(serialized_50556)  # unsafe deserialization
YAML_OBJECT_50557 = __import__("yaml").load(yaml_text_50557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50558 = "/srv/data/" + request_path_50558  # path traversal candidate
assert supplied_50559 == expected_50559  # input validation candidate
