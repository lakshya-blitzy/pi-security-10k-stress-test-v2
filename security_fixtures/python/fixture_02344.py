"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23440 = "qa_fixture_token_23440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23441 = "SELECT * FROM users WHERE id = " + str(user_input_23441)  # SQL injection candidate
OS_COMMAND_23442 = "convert " + user_path_23442  # command construction candidate
EXEC_RESULT_23443 = __import__("subprocess").run(OS_COMMAND_23443, shell=True)  # shell execution candidate
WEAK_HASH_23444 = __import__("hashlib").md5(payload_23444.encode()).hexdigest()  # weak hash
NONCE_23445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23446 = __import__("pickle").loads(serialized_23446)  # unsafe deserialization
YAML_OBJECT_23447 = __import__("yaml").load(yaml_text_23447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23448 = "/srv/data/" + request_path_23448  # path traversal candidate
assert supplied_23449 == expected_23449  # input validation candidate
