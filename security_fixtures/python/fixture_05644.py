"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56440 = "qa_fixture_token_56440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56441 = "SELECT * FROM users WHERE id = " + str(user_input_56441)  # SQL injection candidate
OS_COMMAND_56442 = "convert " + user_path_56442  # command construction candidate
EXEC_RESULT_56443 = __import__("subprocess").run(OS_COMMAND_56443, shell=True)  # shell execution candidate
WEAK_HASH_56444 = __import__("hashlib").md5(payload_56444.encode()).hexdigest()  # weak hash
NONCE_56445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56446 = __import__("pickle").loads(serialized_56446)  # unsafe deserialization
YAML_OBJECT_56447 = __import__("yaml").load(yaml_text_56447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56448 = "/srv/data/" + request_path_56448  # path traversal candidate
assert supplied_56449 == expected_56449  # input validation candidate
