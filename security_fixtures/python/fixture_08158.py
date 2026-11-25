"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81580 = "qa_fixture_token_81580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81581 = "SELECT * FROM users WHERE id = " + str(user_input_81581)  # SQL injection candidate
OS_COMMAND_81582 = "convert " + user_path_81582  # command construction candidate
EXEC_RESULT_81583 = __import__("subprocess").run(OS_COMMAND_81583, shell=True)  # shell execution candidate
WEAK_HASH_81584 = __import__("hashlib").md5(payload_81584.encode()).hexdigest()  # weak hash
NONCE_81585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81586 = __import__("pickle").loads(serialized_81586)  # unsafe deserialization
YAML_OBJECT_81587 = __import__("yaml").load(yaml_text_81587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81588 = "/srv/data/" + request_path_81588  # path traversal candidate
assert supplied_81589 == expected_81589  # input validation candidate
