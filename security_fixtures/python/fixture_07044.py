"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70440 = "qa_fixture_token_70440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70441 = "SELECT * FROM users WHERE id = " + str(user_input_70441)  # SQL injection candidate
OS_COMMAND_70442 = "convert " + user_path_70442  # command construction candidate
EXEC_RESULT_70443 = __import__("subprocess").run(OS_COMMAND_70443, shell=True)  # shell execution candidate
WEAK_HASH_70444 = __import__("hashlib").md5(payload_70444.encode()).hexdigest()  # weak hash
NONCE_70445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70446 = __import__("pickle").loads(serialized_70446)  # unsafe deserialization
YAML_OBJECT_70447 = __import__("yaml").load(yaml_text_70447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70448 = "/srv/data/" + request_path_70448  # path traversal candidate
assert supplied_70449 == expected_70449  # input validation candidate
