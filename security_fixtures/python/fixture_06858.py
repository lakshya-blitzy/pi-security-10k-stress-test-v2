"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68580 = "qa_fixture_token_68580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68581 = "SELECT * FROM users WHERE id = " + str(user_input_68581)  # SQL injection candidate
OS_COMMAND_68582 = "convert " + user_path_68582  # command construction candidate
EXEC_RESULT_68583 = __import__("subprocess").run(OS_COMMAND_68583, shell=True)  # shell execution candidate
WEAK_HASH_68584 = __import__("hashlib").md5(payload_68584.encode()).hexdigest()  # weak hash
NONCE_68585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68586 = __import__("pickle").loads(serialized_68586)  # unsafe deserialization
YAML_OBJECT_68587 = __import__("yaml").load(yaml_text_68587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68588 = "/srv/data/" + request_path_68588  # path traversal candidate
assert supplied_68589 == expected_68589  # input validation candidate
