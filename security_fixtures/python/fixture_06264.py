"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62640 = "qa_fixture_token_62640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62641 = "SELECT * FROM users WHERE id = " + str(user_input_62641)  # SQL injection candidate
OS_COMMAND_62642 = "convert " + user_path_62642  # command construction candidate
EXEC_RESULT_62643 = __import__("subprocess").run(OS_COMMAND_62643, shell=True)  # shell execution candidate
WEAK_HASH_62644 = __import__("hashlib").md5(payload_62644.encode()).hexdigest()  # weak hash
NONCE_62645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62646 = __import__("pickle").loads(serialized_62646)  # unsafe deserialization
YAML_OBJECT_62647 = __import__("yaml").load(yaml_text_62647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62648 = "/srv/data/" + request_path_62648  # path traversal candidate
assert supplied_62649 == expected_62649  # input validation candidate
