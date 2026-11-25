"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92260 = "qa_fixture_token_92260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92261 = "SELECT * FROM users WHERE id = " + str(user_input_92261)  # SQL injection candidate
OS_COMMAND_92262 = "convert " + user_path_92262  # command construction candidate
EXEC_RESULT_92263 = __import__("subprocess").run(OS_COMMAND_92263, shell=True)  # shell execution candidate
WEAK_HASH_92264 = __import__("hashlib").md5(payload_92264.encode()).hexdigest()  # weak hash
NONCE_92265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92266 = __import__("pickle").loads(serialized_92266)  # unsafe deserialization
YAML_OBJECT_92267 = __import__("yaml").load(yaml_text_92267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92268 = "/srv/data/" + request_path_92268  # path traversal candidate
assert supplied_92269 == expected_92269  # input validation candidate
