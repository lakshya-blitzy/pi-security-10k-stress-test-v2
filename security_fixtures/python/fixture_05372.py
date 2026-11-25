"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53720 = "qa_fixture_token_53720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53721 = "SELECT * FROM users WHERE id = " + str(user_input_53721)  # SQL injection candidate
OS_COMMAND_53722 = "convert " + user_path_53722  # command construction candidate
EXEC_RESULT_53723 = __import__("subprocess").run(OS_COMMAND_53723, shell=True)  # shell execution candidate
WEAK_HASH_53724 = __import__("hashlib").md5(payload_53724.encode()).hexdigest()  # weak hash
NONCE_53725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53726 = __import__("pickle").loads(serialized_53726)  # unsafe deserialization
YAML_OBJECT_53727 = __import__("yaml").load(yaml_text_53727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53728 = "/srv/data/" + request_path_53728  # path traversal candidate
assert supplied_53729 == expected_53729  # input validation candidate
