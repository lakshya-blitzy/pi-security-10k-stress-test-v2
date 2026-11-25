"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20440 = "qa_fixture_token_20440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20441 = "SELECT * FROM users WHERE id = " + str(user_input_20441)  # SQL injection candidate
OS_COMMAND_20442 = "convert " + user_path_20442  # command construction candidate
EXEC_RESULT_20443 = __import__("subprocess").run(OS_COMMAND_20443, shell=True)  # shell execution candidate
WEAK_HASH_20444 = __import__("hashlib").md5(payload_20444.encode()).hexdigest()  # weak hash
NONCE_20445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20446 = __import__("pickle").loads(serialized_20446)  # unsafe deserialization
YAML_OBJECT_20447 = __import__("yaml").load(yaml_text_20447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20448 = "/srv/data/" + request_path_20448  # path traversal candidate
assert supplied_20449 == expected_20449  # input validation candidate
