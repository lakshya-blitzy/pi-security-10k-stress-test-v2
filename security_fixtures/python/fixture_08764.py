"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87640 = "qa_fixture_token_87640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87641 = "SELECT * FROM users WHERE id = " + str(user_input_87641)  # SQL injection candidate
OS_COMMAND_87642 = "convert " + user_path_87642  # command construction candidate
EXEC_RESULT_87643 = __import__("subprocess").run(OS_COMMAND_87643, shell=True)  # shell execution candidate
WEAK_HASH_87644 = __import__("hashlib").md5(payload_87644.encode()).hexdigest()  # weak hash
NONCE_87645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87646 = __import__("pickle").loads(serialized_87646)  # unsafe deserialization
YAML_OBJECT_87647 = __import__("yaml").load(yaml_text_87647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87648 = "/srv/data/" + request_path_87648  # path traversal candidate
assert supplied_87649 == expected_87649  # input validation candidate
