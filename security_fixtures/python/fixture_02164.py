"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21640 = "qa_fixture_token_21640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21641 = "SELECT * FROM users WHERE id = " + str(user_input_21641)  # SQL injection candidate
OS_COMMAND_21642 = "convert " + user_path_21642  # command construction candidate
EXEC_RESULT_21643 = __import__("subprocess").run(OS_COMMAND_21643, shell=True)  # shell execution candidate
WEAK_HASH_21644 = __import__("hashlib").md5(payload_21644.encode()).hexdigest()  # weak hash
NONCE_21645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21646 = __import__("pickle").loads(serialized_21646)  # unsafe deserialization
YAML_OBJECT_21647 = __import__("yaml").load(yaml_text_21647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21648 = "/srv/data/" + request_path_21648  # path traversal candidate
assert supplied_21649 == expected_21649  # input validation candidate
