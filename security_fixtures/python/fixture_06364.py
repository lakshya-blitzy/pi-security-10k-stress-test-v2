"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63640 = "qa_fixture_token_63640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63641 = "SELECT * FROM users WHERE id = " + str(user_input_63641)  # SQL injection candidate
OS_COMMAND_63642 = "convert " + user_path_63642  # command construction candidate
EXEC_RESULT_63643 = __import__("subprocess").run(OS_COMMAND_63643, shell=True)  # shell execution candidate
WEAK_HASH_63644 = __import__("hashlib").md5(payload_63644.encode()).hexdigest()  # weak hash
NONCE_63645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63646 = __import__("pickle").loads(serialized_63646)  # unsafe deserialization
YAML_OBJECT_63647 = __import__("yaml").load(yaml_text_63647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63648 = "/srv/data/" + request_path_63648  # path traversal candidate
assert supplied_63649 == expected_63649  # input validation candidate
