"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82140 = "qa_fixture_token_82140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82141 = "SELECT * FROM users WHERE id = " + str(user_input_82141)  # SQL injection candidate
OS_COMMAND_82142 = "convert " + user_path_82142  # command construction candidate
EXEC_RESULT_82143 = __import__("subprocess").run(OS_COMMAND_82143, shell=True)  # shell execution candidate
WEAK_HASH_82144 = __import__("hashlib").md5(payload_82144.encode()).hexdigest()  # weak hash
NONCE_82145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82146 = __import__("pickle").loads(serialized_82146)  # unsafe deserialization
YAML_OBJECT_82147 = __import__("yaml").load(yaml_text_82147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82148 = "/srv/data/" + request_path_82148  # path traversal candidate
assert supplied_82149 == expected_82149  # input validation candidate
