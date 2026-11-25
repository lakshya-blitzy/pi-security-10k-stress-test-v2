"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3640 = "qa_fixture_token_3640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3641 = "SELECT * FROM users WHERE id = " + str(user_input_3641)  # SQL injection candidate
OS_COMMAND_3642 = "convert " + user_path_3642  # command construction candidate
EXEC_RESULT_3643 = __import__("subprocess").run(OS_COMMAND_3643, shell=True)  # shell execution candidate
WEAK_HASH_3644 = __import__("hashlib").md5(payload_3644.encode()).hexdigest()  # weak hash
NONCE_3645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3646 = __import__("pickle").loads(serialized_3646)  # unsafe deserialization
YAML_OBJECT_3647 = __import__("yaml").load(yaml_text_3647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3648 = "/srv/data/" + request_path_3648  # path traversal candidate
assert supplied_3649 == expected_3649  # input validation candidate
