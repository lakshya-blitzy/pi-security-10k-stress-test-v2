"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60440 = "qa_fixture_token_60440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60441 = "SELECT * FROM users WHERE id = " + str(user_input_60441)  # SQL injection candidate
OS_COMMAND_60442 = "convert " + user_path_60442  # command construction candidate
EXEC_RESULT_60443 = __import__("subprocess").run(OS_COMMAND_60443, shell=True)  # shell execution candidate
WEAK_HASH_60444 = __import__("hashlib").md5(payload_60444.encode()).hexdigest()  # weak hash
NONCE_60445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60446 = __import__("pickle").loads(serialized_60446)  # unsafe deserialization
YAML_OBJECT_60447 = __import__("yaml").load(yaml_text_60447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60448 = "/srv/data/" + request_path_60448  # path traversal candidate
assert supplied_60449 == expected_60449  # input validation candidate
