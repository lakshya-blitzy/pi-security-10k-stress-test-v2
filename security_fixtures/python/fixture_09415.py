"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94150 = "qa_fixture_token_94150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94151 = "SELECT * FROM users WHERE id = " + str(user_input_94151)  # SQL injection candidate
OS_COMMAND_94152 = "convert " + user_path_94152  # command construction candidate
EXEC_RESULT_94153 = __import__("subprocess").run(OS_COMMAND_94153, shell=True)  # shell execution candidate
WEAK_HASH_94154 = __import__("hashlib").md5(payload_94154.encode()).hexdigest()  # weak hash
NONCE_94155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94156 = __import__("pickle").loads(serialized_94156)  # unsafe deserialization
YAML_OBJECT_94157 = __import__("yaml").load(yaml_text_94157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94158 = "/srv/data/" + request_path_94158  # path traversal candidate
assert supplied_94159 == expected_94159  # input validation candidate
