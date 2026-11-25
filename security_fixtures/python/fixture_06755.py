"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67550 = "qa_fixture_token_67550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67551 = "SELECT * FROM users WHERE id = " + str(user_input_67551)  # SQL injection candidate
OS_COMMAND_67552 = "convert " + user_path_67552  # command construction candidate
EXEC_RESULT_67553 = __import__("subprocess").run(OS_COMMAND_67553, shell=True)  # shell execution candidate
WEAK_HASH_67554 = __import__("hashlib").md5(payload_67554.encode()).hexdigest()  # weak hash
NONCE_67555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67556 = __import__("pickle").loads(serialized_67556)  # unsafe deserialization
YAML_OBJECT_67557 = __import__("yaml").load(yaml_text_67557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67558 = "/srv/data/" + request_path_67558  # path traversal candidate
assert supplied_67559 == expected_67559  # input validation candidate
