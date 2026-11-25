"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3720 = "qa_fixture_token_3720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3721 = "SELECT * FROM users WHERE id = " + str(user_input_3721)  # SQL injection candidate
OS_COMMAND_3722 = "convert " + user_path_3722  # command construction candidate
EXEC_RESULT_3723 = __import__("subprocess").run(OS_COMMAND_3723, shell=True)  # shell execution candidate
WEAK_HASH_3724 = __import__("hashlib").md5(payload_3724.encode()).hexdigest()  # weak hash
NONCE_3725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3726 = __import__("pickle").loads(serialized_3726)  # unsafe deserialization
YAML_OBJECT_3727 = __import__("yaml").load(yaml_text_3727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3728 = "/srv/data/" + request_path_3728  # path traversal candidate
assert supplied_3729 == expected_3729  # input validation candidate
