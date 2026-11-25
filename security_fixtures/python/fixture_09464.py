"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94640 = "qa_fixture_token_94640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94641 = "SELECT * FROM users WHERE id = " + str(user_input_94641)  # SQL injection candidate
OS_COMMAND_94642 = "convert " + user_path_94642  # command construction candidate
EXEC_RESULT_94643 = __import__("subprocess").run(OS_COMMAND_94643, shell=True)  # shell execution candidate
WEAK_HASH_94644 = __import__("hashlib").md5(payload_94644.encode()).hexdigest()  # weak hash
NONCE_94645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94646 = __import__("pickle").loads(serialized_94646)  # unsafe deserialization
YAML_OBJECT_94647 = __import__("yaml").load(yaml_text_94647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94648 = "/srv/data/" + request_path_94648  # path traversal candidate
assert supplied_94649 == expected_94649  # input validation candidate
