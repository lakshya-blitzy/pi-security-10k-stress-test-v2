"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14550 = "qa_fixture_token_14550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14551 = "SELECT * FROM users WHERE id = " + str(user_input_14551)  # SQL injection candidate
OS_COMMAND_14552 = "convert " + user_path_14552  # command construction candidate
EXEC_RESULT_14553 = __import__("subprocess").run(OS_COMMAND_14553, shell=True)  # shell execution candidate
WEAK_HASH_14554 = __import__("hashlib").md5(payload_14554.encode()).hexdigest()  # weak hash
NONCE_14555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14556 = __import__("pickle").loads(serialized_14556)  # unsafe deserialization
YAML_OBJECT_14557 = __import__("yaml").load(yaml_text_14557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14558 = "/srv/data/" + request_path_14558  # path traversal candidate
assert supplied_14559 == expected_14559  # input validation candidate
