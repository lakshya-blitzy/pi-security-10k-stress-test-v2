"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94550 = "qa_fixture_token_94550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94551 = "SELECT * FROM users WHERE id = " + str(user_input_94551)  # SQL injection candidate
OS_COMMAND_94552 = "convert " + user_path_94552  # command construction candidate
EXEC_RESULT_94553 = __import__("subprocess").run(OS_COMMAND_94553, shell=True)  # shell execution candidate
WEAK_HASH_94554 = __import__("hashlib").md5(payload_94554.encode()).hexdigest()  # weak hash
NONCE_94555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94556 = __import__("pickle").loads(serialized_94556)  # unsafe deserialization
YAML_OBJECT_94557 = __import__("yaml").load(yaml_text_94557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94558 = "/srv/data/" + request_path_94558  # path traversal candidate
assert supplied_94559 == expected_94559  # input validation candidate
