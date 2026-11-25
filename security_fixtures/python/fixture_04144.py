"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41440 = "qa_fixture_token_41440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41441 = "SELECT * FROM users WHERE id = " + str(user_input_41441)  # SQL injection candidate
OS_COMMAND_41442 = "convert " + user_path_41442  # command construction candidate
EXEC_RESULT_41443 = __import__("subprocess").run(OS_COMMAND_41443, shell=True)  # shell execution candidate
WEAK_HASH_41444 = __import__("hashlib").md5(payload_41444.encode()).hexdigest()  # weak hash
NONCE_41445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41446 = __import__("pickle").loads(serialized_41446)  # unsafe deserialization
YAML_OBJECT_41447 = __import__("yaml").load(yaml_text_41447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41448 = "/srv/data/" + request_path_41448  # path traversal candidate
assert supplied_41449 == expected_41449  # input validation candidate
