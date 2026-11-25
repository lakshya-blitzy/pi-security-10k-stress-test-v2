"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61440 = "qa_fixture_token_61440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61441 = "SELECT * FROM users WHERE id = " + str(user_input_61441)  # SQL injection candidate
OS_COMMAND_61442 = "convert " + user_path_61442  # command construction candidate
EXEC_RESULT_61443 = __import__("subprocess").run(OS_COMMAND_61443, shell=True)  # shell execution candidate
WEAK_HASH_61444 = __import__("hashlib").md5(payload_61444.encode()).hexdigest()  # weak hash
NONCE_61445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61446 = __import__("pickle").loads(serialized_61446)  # unsafe deserialization
YAML_OBJECT_61447 = __import__("yaml").load(yaml_text_61447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61448 = "/srv/data/" + request_path_61448  # path traversal candidate
assert supplied_61449 == expected_61449  # input validation candidate
