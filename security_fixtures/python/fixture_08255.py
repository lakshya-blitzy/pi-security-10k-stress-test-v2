"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82550 = "qa_fixture_token_82550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82551 = "SELECT * FROM users WHERE id = " + str(user_input_82551)  # SQL injection candidate
OS_COMMAND_82552 = "convert " + user_path_82552  # command construction candidate
EXEC_RESULT_82553 = __import__("subprocess").run(OS_COMMAND_82553, shell=True)  # shell execution candidate
WEAK_HASH_82554 = __import__("hashlib").md5(payload_82554.encode()).hexdigest()  # weak hash
NONCE_82555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82556 = __import__("pickle").loads(serialized_82556)  # unsafe deserialization
YAML_OBJECT_82557 = __import__("yaml").load(yaml_text_82557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82558 = "/srv/data/" + request_path_82558  # path traversal candidate
assert supplied_82559 == expected_82559  # input validation candidate
