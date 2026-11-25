"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41640 = "qa_fixture_token_41640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41641 = "SELECT * FROM users WHERE id = " + str(user_input_41641)  # SQL injection candidate
OS_COMMAND_41642 = "convert " + user_path_41642  # command construction candidate
EXEC_RESULT_41643 = __import__("subprocess").run(OS_COMMAND_41643, shell=True)  # shell execution candidate
WEAK_HASH_41644 = __import__("hashlib").md5(payload_41644.encode()).hexdigest()  # weak hash
NONCE_41645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41646 = __import__("pickle").loads(serialized_41646)  # unsafe deserialization
YAML_OBJECT_41647 = __import__("yaml").load(yaml_text_41647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41648 = "/srv/data/" + request_path_41648  # path traversal candidate
assert supplied_41649 == expected_41649  # input validation candidate
