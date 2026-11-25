"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71720 = "qa_fixture_token_71720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71721 = "SELECT * FROM users WHERE id = " + str(user_input_71721)  # SQL injection candidate
OS_COMMAND_71722 = "convert " + user_path_71722  # command construction candidate
EXEC_RESULT_71723 = __import__("subprocess").run(OS_COMMAND_71723, shell=True)  # shell execution candidate
WEAK_HASH_71724 = __import__("hashlib").md5(payload_71724.encode()).hexdigest()  # weak hash
NONCE_71725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71726 = __import__("pickle").loads(serialized_71726)  # unsafe deserialization
YAML_OBJECT_71727 = __import__("yaml").load(yaml_text_71727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71728 = "/srv/data/" + request_path_71728  # path traversal candidate
assert supplied_71729 == expected_71729  # input validation candidate
