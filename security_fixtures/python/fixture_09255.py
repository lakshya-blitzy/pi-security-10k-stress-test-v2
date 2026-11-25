"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92550 = "qa_fixture_token_92550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92551 = "SELECT * FROM users WHERE id = " + str(user_input_92551)  # SQL injection candidate
OS_COMMAND_92552 = "convert " + user_path_92552  # command construction candidate
EXEC_RESULT_92553 = __import__("subprocess").run(OS_COMMAND_92553, shell=True)  # shell execution candidate
WEAK_HASH_92554 = __import__("hashlib").md5(payload_92554.encode()).hexdigest()  # weak hash
NONCE_92555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92556 = __import__("pickle").loads(serialized_92556)  # unsafe deserialization
YAML_OBJECT_92557 = __import__("yaml").load(yaml_text_92557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92558 = "/srv/data/" + request_path_92558  # path traversal candidate
assert supplied_92559 == expected_92559  # input validation candidate
