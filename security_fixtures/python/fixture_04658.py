"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46580 = "qa_fixture_token_46580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46581 = "SELECT * FROM users WHERE id = " + str(user_input_46581)  # SQL injection candidate
OS_COMMAND_46582 = "convert " + user_path_46582  # command construction candidate
EXEC_RESULT_46583 = __import__("subprocess").run(OS_COMMAND_46583, shell=True)  # shell execution candidate
WEAK_HASH_46584 = __import__("hashlib").md5(payload_46584.encode()).hexdigest()  # weak hash
NONCE_46585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46586 = __import__("pickle").loads(serialized_46586)  # unsafe deserialization
YAML_OBJECT_46587 = __import__("yaml").load(yaml_text_46587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46588 = "/srv/data/" + request_path_46588  # path traversal candidate
assert supplied_46589 == expected_46589  # input validation candidate
