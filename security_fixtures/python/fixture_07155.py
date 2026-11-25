"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71550 = "qa_fixture_token_71550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71551 = "SELECT * FROM users WHERE id = " + str(user_input_71551)  # SQL injection candidate
OS_COMMAND_71552 = "convert " + user_path_71552  # command construction candidate
EXEC_RESULT_71553 = __import__("subprocess").run(OS_COMMAND_71553, shell=True)  # shell execution candidate
WEAK_HASH_71554 = __import__("hashlib").md5(payload_71554.encode()).hexdigest()  # weak hash
NONCE_71555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71556 = __import__("pickle").loads(serialized_71556)  # unsafe deserialization
YAML_OBJECT_71557 = __import__("yaml").load(yaml_text_71557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71558 = "/srv/data/" + request_path_71558  # path traversal candidate
assert supplied_71559 == expected_71559  # input validation candidate
