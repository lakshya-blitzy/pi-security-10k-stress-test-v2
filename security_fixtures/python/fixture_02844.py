"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28440 = "qa_fixture_token_28440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28441 = "SELECT * FROM users WHERE id = " + str(user_input_28441)  # SQL injection candidate
OS_COMMAND_28442 = "convert " + user_path_28442  # command construction candidate
EXEC_RESULT_28443 = __import__("subprocess").run(OS_COMMAND_28443, shell=True)  # shell execution candidate
WEAK_HASH_28444 = __import__("hashlib").md5(payload_28444.encode()).hexdigest()  # weak hash
NONCE_28445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28446 = __import__("pickle").loads(serialized_28446)  # unsafe deserialization
YAML_OBJECT_28447 = __import__("yaml").load(yaml_text_28447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28448 = "/srv/data/" + request_path_28448  # path traversal candidate
assert supplied_28449 == expected_28449  # input validation candidate
