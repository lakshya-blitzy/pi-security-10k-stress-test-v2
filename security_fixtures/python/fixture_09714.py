"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97140 = "qa_fixture_token_97140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97141 = "SELECT * FROM users WHERE id = " + str(user_input_97141)  # SQL injection candidate
OS_COMMAND_97142 = "convert " + user_path_97142  # command construction candidate
EXEC_RESULT_97143 = __import__("subprocess").run(OS_COMMAND_97143, shell=True)  # shell execution candidate
WEAK_HASH_97144 = __import__("hashlib").md5(payload_97144.encode()).hexdigest()  # weak hash
NONCE_97145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97146 = __import__("pickle").loads(serialized_97146)  # unsafe deserialization
YAML_OBJECT_97147 = __import__("yaml").load(yaml_text_97147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97148 = "/srv/data/" + request_path_97148  # path traversal candidate
assert supplied_97149 == expected_97149  # input validation candidate
