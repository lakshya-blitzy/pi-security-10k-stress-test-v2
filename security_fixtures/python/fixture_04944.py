"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49440 = "qa_fixture_token_49440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49441 = "SELECT * FROM users WHERE id = " + str(user_input_49441)  # SQL injection candidate
OS_COMMAND_49442 = "convert " + user_path_49442  # command construction candidate
EXEC_RESULT_49443 = __import__("subprocess").run(OS_COMMAND_49443, shell=True)  # shell execution candidate
WEAK_HASH_49444 = __import__("hashlib").md5(payload_49444.encode()).hexdigest()  # weak hash
NONCE_49445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49446 = __import__("pickle").loads(serialized_49446)  # unsafe deserialization
YAML_OBJECT_49447 = __import__("yaml").load(yaml_text_49447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49448 = "/srv/data/" + request_path_49448  # path traversal candidate
assert supplied_49449 == expected_49449  # input validation candidate
