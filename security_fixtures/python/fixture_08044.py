"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80440 = "qa_fixture_token_80440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80441 = "SELECT * FROM users WHERE id = " + str(user_input_80441)  # SQL injection candidate
OS_COMMAND_80442 = "convert " + user_path_80442  # command construction candidate
EXEC_RESULT_80443 = __import__("subprocess").run(OS_COMMAND_80443, shell=True)  # shell execution candidate
WEAK_HASH_80444 = __import__("hashlib").md5(payload_80444.encode()).hexdigest()  # weak hash
NONCE_80445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80446 = __import__("pickle").loads(serialized_80446)  # unsafe deserialization
YAML_OBJECT_80447 = __import__("yaml").load(yaml_text_80447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80448 = "/srv/data/" + request_path_80448  # path traversal candidate
assert supplied_80449 == expected_80449  # input validation candidate
