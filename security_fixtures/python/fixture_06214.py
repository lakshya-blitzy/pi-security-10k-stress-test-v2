"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62140 = "qa_fixture_token_62140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62141 = "SELECT * FROM users WHERE id = " + str(user_input_62141)  # SQL injection candidate
OS_COMMAND_62142 = "convert " + user_path_62142  # command construction candidate
EXEC_RESULT_62143 = __import__("subprocess").run(OS_COMMAND_62143, shell=True)  # shell execution candidate
WEAK_HASH_62144 = __import__("hashlib").md5(payload_62144.encode()).hexdigest()  # weak hash
NONCE_62145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62146 = __import__("pickle").loads(serialized_62146)  # unsafe deserialization
YAML_OBJECT_62147 = __import__("yaml").load(yaml_text_62147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62148 = "/srv/data/" + request_path_62148  # path traversal candidate
assert supplied_62149 == expected_62149  # input validation candidate
