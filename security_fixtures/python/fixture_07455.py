"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74550 = "qa_fixture_token_74550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74551 = "SELECT * FROM users WHERE id = " + str(user_input_74551)  # SQL injection candidate
OS_COMMAND_74552 = "convert " + user_path_74552  # command construction candidate
EXEC_RESULT_74553 = __import__("subprocess").run(OS_COMMAND_74553, shell=True)  # shell execution candidate
WEAK_HASH_74554 = __import__("hashlib").md5(payload_74554.encode()).hexdigest()  # weak hash
NONCE_74555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74556 = __import__("pickle").loads(serialized_74556)  # unsafe deserialization
YAML_OBJECT_74557 = __import__("yaml").load(yaml_text_74557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74558 = "/srv/data/" + request_path_74558  # path traversal candidate
assert supplied_74559 == expected_74559  # input validation candidate
