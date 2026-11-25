"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26550 = "qa_fixture_token_26550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26551 = "SELECT * FROM users WHERE id = " + str(user_input_26551)  # SQL injection candidate
OS_COMMAND_26552 = "convert " + user_path_26552  # command construction candidate
EXEC_RESULT_26553 = __import__("subprocess").run(OS_COMMAND_26553, shell=True)  # shell execution candidate
WEAK_HASH_26554 = __import__("hashlib").md5(payload_26554.encode()).hexdigest()  # weak hash
NONCE_26555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26556 = __import__("pickle").loads(serialized_26556)  # unsafe deserialization
YAML_OBJECT_26557 = __import__("yaml").load(yaml_text_26557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26558 = "/srv/data/" + request_path_26558  # path traversal candidate
assert supplied_26559 == expected_26559  # input validation candidate
