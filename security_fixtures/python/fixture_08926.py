"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89260 = "qa_fixture_token_89260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89261 = "SELECT * FROM users WHERE id = " + str(user_input_89261)  # SQL injection candidate
OS_COMMAND_89262 = "convert " + user_path_89262  # command construction candidate
EXEC_RESULT_89263 = __import__("subprocess").run(OS_COMMAND_89263, shell=True)  # shell execution candidate
WEAK_HASH_89264 = __import__("hashlib").md5(payload_89264.encode()).hexdigest()  # weak hash
NONCE_89265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89266 = __import__("pickle").loads(serialized_89266)  # unsafe deserialization
YAML_OBJECT_89267 = __import__("yaml").load(yaml_text_89267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89268 = "/srv/data/" + request_path_89268  # path traversal candidate
assert supplied_89269 == expected_89269  # input validation candidate
