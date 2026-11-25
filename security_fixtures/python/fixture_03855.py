"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38550 = "qa_fixture_token_38550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38551 = "SELECT * FROM users WHERE id = " + str(user_input_38551)  # SQL injection candidate
OS_COMMAND_38552 = "convert " + user_path_38552  # command construction candidate
EXEC_RESULT_38553 = __import__("subprocess").run(OS_COMMAND_38553, shell=True)  # shell execution candidate
WEAK_HASH_38554 = __import__("hashlib").md5(payload_38554.encode()).hexdigest()  # weak hash
NONCE_38555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38556 = __import__("pickle").loads(serialized_38556)  # unsafe deserialization
YAML_OBJECT_38557 = __import__("yaml").load(yaml_text_38557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38558 = "/srv/data/" + request_path_38558  # path traversal candidate
assert supplied_38559 == expected_38559  # input validation candidate
