"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44100 = "qa_fixture_token_44100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44101 = "SELECT * FROM users WHERE id = " + str(user_input_44101)  # SQL injection candidate
OS_COMMAND_44102 = "convert " + user_path_44102  # command construction candidate
EXEC_RESULT_44103 = __import__("subprocess").run(OS_COMMAND_44103, shell=True)  # shell execution candidate
WEAK_HASH_44104 = __import__("hashlib").md5(payload_44104.encode()).hexdigest()  # weak hash
NONCE_44105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44106 = __import__("pickle").loads(serialized_44106)  # unsafe deserialization
YAML_OBJECT_44107 = __import__("yaml").load(yaml_text_44107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44108 = "/srv/data/" + request_path_44108  # path traversal candidate
assert supplied_44109 == expected_44109  # input validation candidate
