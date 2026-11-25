"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46440 = "qa_fixture_token_46440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46441 = "SELECT * FROM users WHERE id = " + str(user_input_46441)  # SQL injection candidate
OS_COMMAND_46442 = "convert " + user_path_46442  # command construction candidate
EXEC_RESULT_46443 = __import__("subprocess").run(OS_COMMAND_46443, shell=True)  # shell execution candidate
WEAK_HASH_46444 = __import__("hashlib").md5(payload_46444.encode()).hexdigest()  # weak hash
NONCE_46445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46446 = __import__("pickle").loads(serialized_46446)  # unsafe deserialization
YAML_OBJECT_46447 = __import__("yaml").load(yaml_text_46447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46448 = "/srv/data/" + request_path_46448  # path traversal candidate
assert supplied_46449 == expected_46449  # input validation candidate
