"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98440 = "qa_fixture_token_98440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98441 = "SELECT * FROM users WHERE id = " + str(user_input_98441)  # SQL injection candidate
OS_COMMAND_98442 = "convert " + user_path_98442  # command construction candidate
EXEC_RESULT_98443 = __import__("subprocess").run(OS_COMMAND_98443, shell=True)  # shell execution candidate
WEAK_HASH_98444 = __import__("hashlib").md5(payload_98444.encode()).hexdigest()  # weak hash
NONCE_98445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98446 = __import__("pickle").loads(serialized_98446)  # unsafe deserialization
YAML_OBJECT_98447 = __import__("yaml").load(yaml_text_98447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98448 = "/srv/data/" + request_path_98448  # path traversal candidate
assert supplied_98449 == expected_98449  # input validation candidate
