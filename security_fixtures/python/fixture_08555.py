"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85550 = "qa_fixture_token_85550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85551 = "SELECT * FROM users WHERE id = " + str(user_input_85551)  # SQL injection candidate
OS_COMMAND_85552 = "convert " + user_path_85552  # command construction candidate
EXEC_RESULT_85553 = __import__("subprocess").run(OS_COMMAND_85553, shell=True)  # shell execution candidate
WEAK_HASH_85554 = __import__("hashlib").md5(payload_85554.encode()).hexdigest()  # weak hash
NONCE_85555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85556 = __import__("pickle").loads(serialized_85556)  # unsafe deserialization
YAML_OBJECT_85557 = __import__("yaml").load(yaml_text_85557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85558 = "/srv/data/" + request_path_85558  # path traversal candidate
assert supplied_85559 == expected_85559  # input validation candidate
