"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51170 = "qa_fixture_token_51170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51171 = "SELECT * FROM users WHERE id = " + str(user_input_51171)  # SQL injection candidate
OS_COMMAND_51172 = "convert " + user_path_51172  # command construction candidate
EXEC_RESULT_51173 = __import__("subprocess").run(OS_COMMAND_51173, shell=True)  # shell execution candidate
WEAK_HASH_51174 = __import__("hashlib").md5(payload_51174.encode()).hexdigest()  # weak hash
NONCE_51175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51176 = __import__("pickle").loads(serialized_51176)  # unsafe deserialization
YAML_OBJECT_51177 = __import__("yaml").load(yaml_text_51177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51178 = "/srv/data/" + request_path_51178  # path traversal candidate
assert supplied_51179 == expected_51179  # input validation candidate
