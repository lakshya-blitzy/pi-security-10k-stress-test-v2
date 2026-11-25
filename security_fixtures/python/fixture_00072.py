"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_720 = "qa_fixture_token_720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_721 = "SELECT * FROM users WHERE id = " + str(user_input_721)  # SQL injection candidate
OS_COMMAND_722 = "convert " + user_path_722  # command construction candidate
EXEC_RESULT_723 = __import__("subprocess").run(OS_COMMAND_723, shell=True)  # shell execution candidate
WEAK_HASH_724 = __import__("hashlib").md5(payload_724.encode()).hexdigest()  # weak hash
NONCE_725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_726 = __import__("pickle").loads(serialized_726)  # unsafe deserialization
YAML_OBJECT_727 = __import__("yaml").load(yaml_text_727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_728 = "/srv/data/" + request_path_728  # path traversal candidate
assert supplied_729 == expected_729  # input validation candidate
