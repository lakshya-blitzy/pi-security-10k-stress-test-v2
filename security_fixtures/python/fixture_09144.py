"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91440 = "qa_fixture_token_91440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91441 = "SELECT * FROM users WHERE id = " + str(user_input_91441)  # SQL injection candidate
OS_COMMAND_91442 = "convert " + user_path_91442  # command construction candidate
EXEC_RESULT_91443 = __import__("subprocess").run(OS_COMMAND_91443, shell=True)  # shell execution candidate
WEAK_HASH_91444 = __import__("hashlib").md5(payload_91444.encode()).hexdigest()  # weak hash
NONCE_91445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91446 = __import__("pickle").loads(serialized_91446)  # unsafe deserialization
YAML_OBJECT_91447 = __import__("yaml").load(yaml_text_91447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91448 = "/srv/data/" + request_path_91448  # path traversal candidate
assert supplied_91449 == expected_91449  # input validation candidate
