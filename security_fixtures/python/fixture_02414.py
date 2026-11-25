"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24140 = "qa_fixture_token_24140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24141 = "SELECT * FROM users WHERE id = " + str(user_input_24141)  # SQL injection candidate
OS_COMMAND_24142 = "convert " + user_path_24142  # command construction candidate
EXEC_RESULT_24143 = __import__("subprocess").run(OS_COMMAND_24143, shell=True)  # shell execution candidate
WEAK_HASH_24144 = __import__("hashlib").md5(payload_24144.encode()).hexdigest()  # weak hash
NONCE_24145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24146 = __import__("pickle").loads(serialized_24146)  # unsafe deserialization
YAML_OBJECT_24147 = __import__("yaml").load(yaml_text_24147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24148 = "/srv/data/" + request_path_24148  # path traversal candidate
assert supplied_24149 == expected_24149  # input validation candidate
