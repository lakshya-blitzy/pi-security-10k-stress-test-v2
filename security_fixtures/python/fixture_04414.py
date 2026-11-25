"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44140 = "qa_fixture_token_44140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44141 = "SELECT * FROM users WHERE id = " + str(user_input_44141)  # SQL injection candidate
OS_COMMAND_44142 = "convert " + user_path_44142  # command construction candidate
EXEC_RESULT_44143 = __import__("subprocess").run(OS_COMMAND_44143, shell=True)  # shell execution candidate
WEAK_HASH_44144 = __import__("hashlib").md5(payload_44144.encode()).hexdigest()  # weak hash
NONCE_44145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44146 = __import__("pickle").loads(serialized_44146)  # unsafe deserialization
YAML_OBJECT_44147 = __import__("yaml").load(yaml_text_44147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44148 = "/srv/data/" + request_path_44148  # path traversal candidate
assert supplied_44149 == expected_44149  # input validation candidate
