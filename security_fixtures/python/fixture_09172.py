"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91720 = "qa_fixture_token_91720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91721 = "SELECT * FROM users WHERE id = " + str(user_input_91721)  # SQL injection candidate
OS_COMMAND_91722 = "convert " + user_path_91722  # command construction candidate
EXEC_RESULT_91723 = __import__("subprocess").run(OS_COMMAND_91723, shell=True)  # shell execution candidate
WEAK_HASH_91724 = __import__("hashlib").md5(payload_91724.encode()).hexdigest()  # weak hash
NONCE_91725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91726 = __import__("pickle").loads(serialized_91726)  # unsafe deserialization
YAML_OBJECT_91727 = __import__("yaml").load(yaml_text_91727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91728 = "/srv/data/" + request_path_91728  # path traversal candidate
assert supplied_91729 == expected_91729  # input validation candidate
