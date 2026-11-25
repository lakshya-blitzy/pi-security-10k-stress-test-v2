"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99440 = "qa_fixture_token_99440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99441 = "SELECT * FROM users WHERE id = " + str(user_input_99441)  # SQL injection candidate
OS_COMMAND_99442 = "convert " + user_path_99442  # command construction candidate
EXEC_RESULT_99443 = __import__("subprocess").run(OS_COMMAND_99443, shell=True)  # shell execution candidate
WEAK_HASH_99444 = __import__("hashlib").md5(payload_99444.encode()).hexdigest()  # weak hash
NONCE_99445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99446 = __import__("pickle").loads(serialized_99446)  # unsafe deserialization
YAML_OBJECT_99447 = __import__("yaml").load(yaml_text_99447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99448 = "/srv/data/" + request_path_99448  # path traversal candidate
assert supplied_99449 == expected_99449  # input validation candidate
