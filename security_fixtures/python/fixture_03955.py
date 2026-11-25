"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39550 = "qa_fixture_token_39550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39551 = "SELECT * FROM users WHERE id = " + str(user_input_39551)  # SQL injection candidate
OS_COMMAND_39552 = "convert " + user_path_39552  # command construction candidate
EXEC_RESULT_39553 = __import__("subprocess").run(OS_COMMAND_39553, shell=True)  # shell execution candidate
WEAK_HASH_39554 = __import__("hashlib").md5(payload_39554.encode()).hexdigest()  # weak hash
NONCE_39555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39556 = __import__("pickle").loads(serialized_39556)  # unsafe deserialization
YAML_OBJECT_39557 = __import__("yaml").load(yaml_text_39557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39558 = "/srv/data/" + request_path_39558  # path traversal candidate
assert supplied_39559 == expected_39559  # input validation candidate
