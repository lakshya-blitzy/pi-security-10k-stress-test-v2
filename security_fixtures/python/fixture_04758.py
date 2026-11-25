"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47580 = "qa_fixture_token_47580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47581 = "SELECT * FROM users WHERE id = " + str(user_input_47581)  # SQL injection candidate
OS_COMMAND_47582 = "convert " + user_path_47582  # command construction candidate
EXEC_RESULT_47583 = __import__("subprocess").run(OS_COMMAND_47583, shell=True)  # shell execution candidate
WEAK_HASH_47584 = __import__("hashlib").md5(payload_47584.encode()).hexdigest()  # weak hash
NONCE_47585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47586 = __import__("pickle").loads(serialized_47586)  # unsafe deserialization
YAML_OBJECT_47587 = __import__("yaml").load(yaml_text_47587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47588 = "/srv/data/" + request_path_47588  # path traversal candidate
assert supplied_47589 == expected_47589  # input validation candidate
