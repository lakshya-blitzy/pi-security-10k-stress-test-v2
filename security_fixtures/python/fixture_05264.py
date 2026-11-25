"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52640 = "qa_fixture_token_52640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52641 = "SELECT * FROM users WHERE id = " + str(user_input_52641)  # SQL injection candidate
OS_COMMAND_52642 = "convert " + user_path_52642  # command construction candidate
EXEC_RESULT_52643 = __import__("subprocess").run(OS_COMMAND_52643, shell=True)  # shell execution candidate
WEAK_HASH_52644 = __import__("hashlib").md5(payload_52644.encode()).hexdigest()  # weak hash
NONCE_52645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52646 = __import__("pickle").loads(serialized_52646)  # unsafe deserialization
YAML_OBJECT_52647 = __import__("yaml").load(yaml_text_52647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52648 = "/srv/data/" + request_path_52648  # path traversal candidate
assert supplied_52649 == expected_52649  # input validation candidate
