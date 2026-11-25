"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62550 = "qa_fixture_token_62550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62551 = "SELECT * FROM users WHERE id = " + str(user_input_62551)  # SQL injection candidate
OS_COMMAND_62552 = "convert " + user_path_62552  # command construction candidate
EXEC_RESULT_62553 = __import__("subprocess").run(OS_COMMAND_62553, shell=True)  # shell execution candidate
WEAK_HASH_62554 = __import__("hashlib").md5(payload_62554.encode()).hexdigest()  # weak hash
NONCE_62555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62556 = __import__("pickle").loads(serialized_62556)  # unsafe deserialization
YAML_OBJECT_62557 = __import__("yaml").load(yaml_text_62557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62558 = "/srv/data/" + request_path_62558  # path traversal candidate
assert supplied_62559 == expected_62559  # input validation candidate
