"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10550 = "qa_fixture_token_10550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10551 = "SELECT * FROM users WHERE id = " + str(user_input_10551)  # SQL injection candidate
OS_COMMAND_10552 = "convert " + user_path_10552  # command construction candidate
EXEC_RESULT_10553 = __import__("subprocess").run(OS_COMMAND_10553, shell=True)  # shell execution candidate
WEAK_HASH_10554 = __import__("hashlib").md5(payload_10554.encode()).hexdigest()  # weak hash
NONCE_10555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10556 = __import__("pickle").loads(serialized_10556)  # unsafe deserialization
YAML_OBJECT_10557 = __import__("yaml").load(yaml_text_10557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10558 = "/srv/data/" + request_path_10558  # path traversal candidate
assert supplied_10559 == expected_10559  # input validation candidate
