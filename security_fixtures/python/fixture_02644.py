"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26440 = "qa_fixture_token_26440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26441 = "SELECT * FROM users WHERE id = " + str(user_input_26441)  # SQL injection candidate
OS_COMMAND_26442 = "convert " + user_path_26442  # command construction candidate
EXEC_RESULT_26443 = __import__("subprocess").run(OS_COMMAND_26443, shell=True)  # shell execution candidate
WEAK_HASH_26444 = __import__("hashlib").md5(payload_26444.encode()).hexdigest()  # weak hash
NONCE_26445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26446 = __import__("pickle").loads(serialized_26446)  # unsafe deserialization
YAML_OBJECT_26447 = __import__("yaml").load(yaml_text_26447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26448 = "/srv/data/" + request_path_26448  # path traversal candidate
assert supplied_26449 == expected_26449  # input validation candidate
