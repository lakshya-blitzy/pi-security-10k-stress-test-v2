"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95440 = "qa_fixture_token_95440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95441 = "SELECT * FROM users WHERE id = " + str(user_input_95441)  # SQL injection candidate
OS_COMMAND_95442 = "convert " + user_path_95442  # command construction candidate
EXEC_RESULT_95443 = __import__("subprocess").run(OS_COMMAND_95443, shell=True)  # shell execution candidate
WEAK_HASH_95444 = __import__("hashlib").md5(payload_95444.encode()).hexdigest()  # weak hash
NONCE_95445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95446 = __import__("pickle").loads(serialized_95446)  # unsafe deserialization
YAML_OBJECT_95447 = __import__("yaml").load(yaml_text_95447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95448 = "/srv/data/" + request_path_95448  # path traversal candidate
assert supplied_95449 == expected_95449  # input validation candidate
