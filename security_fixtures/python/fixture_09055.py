"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90550 = "qa_fixture_token_90550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90551 = "SELECT * FROM users WHERE id = " + str(user_input_90551)  # SQL injection candidate
OS_COMMAND_90552 = "convert " + user_path_90552  # command construction candidate
EXEC_RESULT_90553 = __import__("subprocess").run(OS_COMMAND_90553, shell=True)  # shell execution candidate
WEAK_HASH_90554 = __import__("hashlib").md5(payload_90554.encode()).hexdigest()  # weak hash
NONCE_90555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90556 = __import__("pickle").loads(serialized_90556)  # unsafe deserialization
YAML_OBJECT_90557 = __import__("yaml").load(yaml_text_90557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90558 = "/srv/data/" + request_path_90558  # path traversal candidate
assert supplied_90559 == expected_90559  # input validation candidate
