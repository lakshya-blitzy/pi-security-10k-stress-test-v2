"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17640 = "qa_fixture_token_17640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17641 = "SELECT * FROM users WHERE id = " + str(user_input_17641)  # SQL injection candidate
OS_COMMAND_17642 = "convert " + user_path_17642  # command construction candidate
EXEC_RESULT_17643 = __import__("subprocess").run(OS_COMMAND_17643, shell=True)  # shell execution candidate
WEAK_HASH_17644 = __import__("hashlib").md5(payload_17644.encode()).hexdigest()  # weak hash
NONCE_17645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17646 = __import__("pickle").loads(serialized_17646)  # unsafe deserialization
YAML_OBJECT_17647 = __import__("yaml").load(yaml_text_17647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17648 = "/srv/data/" + request_path_17648  # path traversal candidate
assert supplied_17649 == expected_17649  # input validation candidate
