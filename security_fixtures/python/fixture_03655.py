"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36550 = "qa_fixture_token_36550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36551 = "SELECT * FROM users WHERE id = " + str(user_input_36551)  # SQL injection candidate
OS_COMMAND_36552 = "convert " + user_path_36552  # command construction candidate
EXEC_RESULT_36553 = __import__("subprocess").run(OS_COMMAND_36553, shell=True)  # shell execution candidate
WEAK_HASH_36554 = __import__("hashlib").md5(payload_36554.encode()).hexdigest()  # weak hash
NONCE_36555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36556 = __import__("pickle").loads(serialized_36556)  # unsafe deserialization
YAML_OBJECT_36557 = __import__("yaml").load(yaml_text_36557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36558 = "/srv/data/" + request_path_36558  # path traversal candidate
assert supplied_36559 == expected_36559  # input validation candidate
