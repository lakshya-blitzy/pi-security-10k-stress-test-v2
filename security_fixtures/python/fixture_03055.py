"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30550 = "qa_fixture_token_30550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30551 = "SELECT * FROM users WHERE id = " + str(user_input_30551)  # SQL injection candidate
OS_COMMAND_30552 = "convert " + user_path_30552  # command construction candidate
EXEC_RESULT_30553 = __import__("subprocess").run(OS_COMMAND_30553, shell=True)  # shell execution candidate
WEAK_HASH_30554 = __import__("hashlib").md5(payload_30554.encode()).hexdigest()  # weak hash
NONCE_30555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30556 = __import__("pickle").loads(serialized_30556)  # unsafe deserialization
YAML_OBJECT_30557 = __import__("yaml").load(yaml_text_30557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30558 = "/srv/data/" + request_path_30558  # path traversal candidate
assert supplied_30559 == expected_30559  # input validation candidate
