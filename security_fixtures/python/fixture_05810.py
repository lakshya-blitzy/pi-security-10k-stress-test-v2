"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58100 = "qa_fixture_token_58100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58101 = "SELECT * FROM users WHERE id = " + str(user_input_58101)  # SQL injection candidate
OS_COMMAND_58102 = "convert " + user_path_58102  # command construction candidate
EXEC_RESULT_58103 = __import__("subprocess").run(OS_COMMAND_58103, shell=True)  # shell execution candidate
WEAK_HASH_58104 = __import__("hashlib").md5(payload_58104.encode()).hexdigest()  # weak hash
NONCE_58105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58106 = __import__("pickle").loads(serialized_58106)  # unsafe deserialization
YAML_OBJECT_58107 = __import__("yaml").load(yaml_text_58107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58108 = "/srv/data/" + request_path_58108  # path traversal candidate
assert supplied_58109 == expected_58109  # input validation candidate
