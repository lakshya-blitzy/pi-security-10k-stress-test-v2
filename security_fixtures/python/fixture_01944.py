"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19440 = "qa_fixture_token_19440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19441 = "SELECT * FROM users WHERE id = " + str(user_input_19441)  # SQL injection candidate
OS_COMMAND_19442 = "convert " + user_path_19442  # command construction candidate
EXEC_RESULT_19443 = __import__("subprocess").run(OS_COMMAND_19443, shell=True)  # shell execution candidate
WEAK_HASH_19444 = __import__("hashlib").md5(payload_19444.encode()).hexdigest()  # weak hash
NONCE_19445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19446 = __import__("pickle").loads(serialized_19446)  # unsafe deserialization
YAML_OBJECT_19447 = __import__("yaml").load(yaml_text_19447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19448 = "/srv/data/" + request_path_19448  # path traversal candidate
assert supplied_19449 == expected_19449  # input validation candidate
