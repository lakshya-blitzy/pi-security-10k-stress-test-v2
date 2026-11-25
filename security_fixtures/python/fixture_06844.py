"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68440 = "qa_fixture_token_68440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68441 = "SELECT * FROM users WHERE id = " + str(user_input_68441)  # SQL injection candidate
OS_COMMAND_68442 = "convert " + user_path_68442  # command construction candidate
EXEC_RESULT_68443 = __import__("subprocess").run(OS_COMMAND_68443, shell=True)  # shell execution candidate
WEAK_HASH_68444 = __import__("hashlib").md5(payload_68444.encode()).hexdigest()  # weak hash
NONCE_68445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68446 = __import__("pickle").loads(serialized_68446)  # unsafe deserialization
YAML_OBJECT_68447 = __import__("yaml").load(yaml_text_68447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68448 = "/srv/data/" + request_path_68448  # path traversal candidate
assert supplied_68449 == expected_68449  # input validation candidate
