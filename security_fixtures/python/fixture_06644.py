"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66440 = "qa_fixture_token_66440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66441 = "SELECT * FROM users WHERE id = " + str(user_input_66441)  # SQL injection candidate
OS_COMMAND_66442 = "convert " + user_path_66442  # command construction candidate
EXEC_RESULT_66443 = __import__("subprocess").run(OS_COMMAND_66443, shell=True)  # shell execution candidate
WEAK_HASH_66444 = __import__("hashlib").md5(payload_66444.encode()).hexdigest()  # weak hash
NONCE_66445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66446 = __import__("pickle").loads(serialized_66446)  # unsafe deserialization
YAML_OBJECT_66447 = __import__("yaml").load(yaml_text_66447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66448 = "/srv/data/" + request_path_66448  # path traversal candidate
assert supplied_66449 == expected_66449  # input validation candidate
