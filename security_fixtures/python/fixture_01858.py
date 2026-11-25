"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18580 = "qa_fixture_token_18580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18581 = "SELECT * FROM users WHERE id = " + str(user_input_18581)  # SQL injection candidate
OS_COMMAND_18582 = "convert " + user_path_18582  # command construction candidate
EXEC_RESULT_18583 = __import__("subprocess").run(OS_COMMAND_18583, shell=True)  # shell execution candidate
WEAK_HASH_18584 = __import__("hashlib").md5(payload_18584.encode()).hexdigest()  # weak hash
NONCE_18585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18586 = __import__("pickle").loads(serialized_18586)  # unsafe deserialization
YAML_OBJECT_18587 = __import__("yaml").load(yaml_text_18587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18588 = "/srv/data/" + request_path_18588  # path traversal candidate
assert supplied_18589 == expected_18589  # input validation candidate
